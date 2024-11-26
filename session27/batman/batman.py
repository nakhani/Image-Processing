import cv2
import numpy as np


image = cv2.imread("batman/image.jpg", 0)
image =cv2.resize(image,(450,250))

_,image = cv2.threshold(image, 82, 255,cv2.THRESH_BINARY_INV)

cv2.putText(image, "BATMAN", (image.shape[1]//2-25, 210), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2, cv2.LINE_AA)


cv2.imshow("result", image)
cv2.imwrite("batman/batman.jpg",image)
cv2.waitKey(0)
