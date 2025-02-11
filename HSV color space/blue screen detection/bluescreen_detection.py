import cv2
import numpy as np


superman_image = cv2.imread('image.png')
background_image = cv2.imread('clouds-8459053_1280.jpg')


rows, cols, channels = superman_image.shape


background_image = cv2.resize(background_image, (cols, rows))


hsv_superman = cv2.cvtColor(superman_image, cv2.COLOR_BGR2HSV)


lower_green = np.array([35, 50, 50])
upper_green = np.array([80, 255, 255])


mask = cv2.inRange(hsv_superman, lower_green, upper_green)


mask_inv = cv2.bitwise_not(mask)


superman_fg = cv2.bitwise_and(superman_image, superman_image, mask=mask_inv)


roi = background_image[0:rows, 0:cols]

background_bg = cv2.bitwise_and(roi, roi, mask=mask)

result = cv2.add(superman_fg, background_bg)


background_image[0:rows, 0:cols] = result

cv2.imwrite("result.png", background_image)
cv2.imshow('Superman', background_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

