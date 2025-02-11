import cv2
import numpy as np
from imutils import resize


def skin_detection(frame):

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower = np.array([0, 48, 80], dtype="uint8")
    upper = np.array([20, 255, 255], dtype="uint8")

    skin_mask = cv2.inRange(hsv_frame, lower, upper)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    skin_mask = cv2.erode(skin_mask, kernel, iterations=2)
    skin_mask = cv2.dilate(skin_mask, kernel, iterations=2)

    skin_mask = cv2.GaussianBlur(skin_mask, (3, 3), 0)

    skin = cv2.bitwise_and(frame, frame, mask=skin_mask)

    return skin

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        break
    frame = resize(frame, width = 400)
    skin_frame = skin_detection(frame)

    cv2.imshow('Skin Detection', skin_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()