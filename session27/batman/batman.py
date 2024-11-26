import cv2
import numpy as np


image = cv2.imread("batman/image.jpg", 0)
image =cv2.resize(image,(400,200))

_,image = cv2.threshold(image, 82, 255,cv2.THRESH_BINARY_INV)

cv2.imshow("result", image)
cv2.imwrite("batman/batman.jpg",image)
cv2.waitKey(0)
