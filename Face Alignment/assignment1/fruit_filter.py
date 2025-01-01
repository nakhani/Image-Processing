import numpy as np
import cv2
import time
from TFLiteFaceDetector import UltraLightFaceDetecion
from TFLiteFaceAlignment import CoordinateAlignmentModel

image = cv2.imread("input/person.jpg")
image_fruit = cv2.imread("input/orange.jpg")

image = cv2.resize(image, (800, 800))
image_fruit = cv2.resize(image_fruit, (800, 800))

lips = [52, 64, 63, 71, 67, 68, 61, 58, 59, 53, 56, 55]
right_eye = [89, 95, 94, 96, 93, 91, 87, 90]
left_eye = [35, 41, 40, 42, 39, 37, 33, 36]

def transparent(landmarks, image):
    x, y, w, h = cv2.boundingRect(landmarks)
    mask = np.zeros(image.shape[:2], dtype=np.uint8)
    cv2.drawContours(mask, [landmarks], -1, (255), -1)
    mask = mask // 255

    result = image * mask[:, :, np.newaxis]
    result = result[y:y + h, x:x + w]

    transparent_mask = np.zeros((result.shape[0], result.shape[1], 4), dtype=np.uint8)
    transparent_mask[:, :, :3] = result
    transparent_mask[:, :, 3] = cv2.resize(mask[y:y + h, x:x + w], (result.shape[1], result.shape[0])) * 255

    return transparent_mask, (x, y, w, h)

def merge_transparent(background, overlay, x, y):
    bh, bw = background.shape[:2]
    oh, ow = overlay.shape[:2]

    if x >= bw or y >= bh or x + ow <= 0 or y + oh <= 0:
        return background

    b = background[y:y+oh, x:x+ow]
    alpha = overlay[:, :, 3] / 255.0

    overlay_image = overlay[:, :, :3]
    for c in range(3):
        b[:, :, c] = b[:, :, c] * (1 - alpha) + overlay_image[:, :, c] * alpha

    background[y:y+oh, x:x+ow] = b
    return background

def filter(points_list):
    fd = UltraLightFaceDetecion("weights/RFB-320.tflite", conf_threshold=0.88)
    fa = CoordinateAlignmentModel("weights/coor_2d106.tflite")

    boxes, scores = fd.inference(image)

    for pred in fa.get_landmarks(image, boxes):
        for points in points_list:
            landmarks = np.array([pred[i] for i in points], dtype=int)
            result, position = transparent(landmarks, image)
            x, y, w, h = position

            
            merge_transparent(image_fruit, result, x, y)

    cv2.imshow("result", image_fruit)
    cv2.waitKey()
    cv2.imwrite("output/result.jpg", image_fruit)


filter([lips, right_eye, left_eye])
