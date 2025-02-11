import cv2
import numpy as np


colors_hsv = {
    "Red": [(0, 70, 50), (10, 255, 255)], 
    "Red2": [(170, 70, 50), (180, 255, 255)], 
    "Green": [(36, 40, 40), (70, 255, 255)], 
    "Blue": [(90, 50, 50), (128, 255, 255)], 
    "Yellow": [(22, 93, 0), (45, 255, 255)], 
    "Orange": [(10, 100, 20), (25, 255, 255)], 
    "Purple": [(129, 50, 70), (158, 255, 255)], 
    "White": [(0, 0, 200), (180, 20, 255)], 
    "Black": [(0, 0, 0), (180, 255, 30)] 
}

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('detector/output.mp4', fourcc, 20.0, (640, 480))

while True:
    _, frame = cap.read()
    
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape
    
    rect_width, rect_height = 100, 100
    rect_x = width // 2 - rect_width // 2
    rect_y = height // 2 - rect_height // 2
    
    blurred_frame = cv2.GaussianBlur(frame, (51, 51), 20)
    blurred_frame[rect_y:rect_y + rect_height, rect_x:rect_x + rect_width] = frame[rect_y:rect_y + rect_height, rect_x:rect_x + rect_width]
    
    point = hsv_frame[rect_y:rect_y + rect_height, rect_x:rect_x + rect_width]
    
    max_sum = -1
    detected_color = "Undefined"
    
    for color, (lower, upper) in colors_hsv.items():
        mask = cv2.inRange(point, np.array(lower), np.array(upper))
        color_sum = np.sum(mask)
        if color_sum > max_sum:
            max_sum = color_sum
            detected_color = color

    mask_red1 = cv2.inRange(point, np.array(colors_hsv["Red"][0]), np.array(colors_hsv["Red"][1]))
    mask_red2 = cv2.inRange(point, np.array(colors_hsv["Red2"][0]), np.array(colors_hsv["Red2"][1]))
    mask_red = mask_red1 + mask_red2
    if np.sum(mask_red) > max_sum:
        detected_color = "Red"
    
    cv2.rectangle(blurred_frame, (rect_x, rect_y), (rect_x + rect_width, rect_y + rect_height), (0, 0, 0), 2)
    cv2.putText(blurred_frame, detected_color, (rect_x, rect_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 0), 2, cv2.LINE_AA)
    
    out.write(blurred_frame)
    cv2.imshow("Detector", blurred_frame)
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
