import numpy as np
import cv2
import time
from TFLiteFaceDetector import UltraLightFaceDetecion
from TFLiteFaceAlignment import CoordinateAlignmentModel

def zoom(landmarks, image, factor=2):
    x, y, w, h = cv2.boundingRect(landmarks)
    mask = np.zeros(image.shape[:2], dtype=np.uint8)
    cv2.drawContours(mask, [landmarks], -1, (255), -1)
    mask = mask // 255
    result = image * mask[:, :, np.newaxis]
    result = result[y:y + h, x:x + w]
    result_big = cv2.resize(result, (0, 0), fx=factor, fy=factor)
    
    transparent_mask = np.zeros((result_big.shape[0], result_big.shape[1], 4), dtype=np.uint8)
    transparent_mask[:,:,:3] = result_big
    transparent_mask[:,:,3] = cv2.resize(mask[y:y + h, x:x + w], (result_big.shape[1], result_big.shape[0])) * 255
    
    return transparent_mask, (x, y, w, h)

def overlay_zoom(transparent_mask, image, position):
    x, y, w, h = position
    zoomed_h, zoomed_w = transparent_mask.shape[:2]
    x_center = x + w // 2
    y_center = y + h // 2
    x_new = x_center - zoomed_w // 2
    y_new = y_center - zoomed_h // 2
    
    alpha = transparent_mask[:, :, 3] / 255.0
    for c in range(0, 3):
        image[y_new:y_new + zoomed_h, x_new:x_new + zoomed_w, c] = alpha * transparent_mask[:, :, c] + (1 - alpha) * image[y_new:y_new + zoomed_h, x_new:x_new + zoomed_w, c]
    return image

def lips_zoom(pred, image):
    lips_landmarks = [] 
    for i in [52, 64, 63, 71, 67, 68, 61, 58, 59, 53, 56, 55]:
        lips_landmarks.append(pred[i])
    lips_landmarks = np.array(lips_landmarks, dtype=int)
    result, position = zoom(lips_landmarks, image)
    image = overlay_zoom(result, image, position)
    return image

def righteye_zoom(pred, image):
    right_eye_landmarks = []  
    for i in [89, 95, 94, 96, 93, 91, 87, 90]:
        right_eye_landmarks.append(pred[i])
    right_eye_landmarks = np.array(right_eye_landmarks, dtype=int)
    result, position = zoom(right_eye_landmarks, image)
    image = overlay_zoom(result, image, position)
    return image

def lefteye_zoom(pred, image):
    left_eye_landmarks = []  
    for i in [35, 41, 40, 42, 39, 37, 33, 36]:
        left_eye_landmarks.append(pred[i])
    left_eye_landmarks = np.array(left_eye_landmarks, dtype=int)
    result, position = zoom(left_eye_landmarks, image)
    image = overlay_zoom(result, image, position)
    return image

fd = UltraLightFaceDetecion("weights/RFB-320.tflite", conf_threshold=0.88)
fa = CoordinateAlignmentModel("weights/coor_2d106.tflite")

image = cv2.imread("input/person.jpg")

start_time = time.perf_counter()

boxes, scores = fd.inference(image)

for pred in fa.get_landmarks(image, boxes):
    image = lips_zoom(pred, image)
    image = righteye_zoom(pred, image)
    image = lefteye_zoom(pred, image)
    
print(time.perf_counter() - start_time)

cv2.imshow("Result", image)
cv2.waitKey()
cv2.imwrite("output/result2.jpg", image)
