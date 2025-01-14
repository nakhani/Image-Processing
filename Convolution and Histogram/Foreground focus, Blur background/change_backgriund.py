import numpy as np
import cv2


image = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)


rows, cols = image.shape
result = np.zeros((rows, cols), dtype=np.uint8)


blurred_image = cv2.GaussianBlur(image, (21, 21), 0)


_, mask = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

kernel = np.ones((5, 5), np.uint8)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)


mask_inv = cv2.bitwise_not(mask)


result = cv2.bitwise_and(image, image, mask=mask) + cv2.bitwise_and(blurred_image, blurred_image, mask=mask_inv)

cv2.imwrite("result.png", result)

