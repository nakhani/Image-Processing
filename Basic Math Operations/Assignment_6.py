import cv2
import numpy as np

image_home = cv2.imread("inputs/home.jpg", cv2.IMREAD_COLOR)
image_home_mask = cv2.imread("inputs/home_mask.jpg", cv2.IMREAD_COLOR)
image_home_floor = cv2.imread("inputs/home_floor.jpg", cv2.IMREAD_COLOR)


image_home_mask = cv2.resize(image_home_mask, (image_home.shape[1], image_home.shape[0]))
image_home_floor = cv2.resize(image_home_floor, (image_home.shape[1], image_home.shape[0]))

image_home = image_home.astype(np.float32)
image_home_mask = image_home_mask.astype(np.float32) / 255  
image_home_floor = image_home_floor.astype(np.float32)


image_home_mask_inv = 1 - image_home_mask

blended_home = cv2.multiply(image_home, image_home_mask_inv)
blended_floor = cv2.multiply(image_home_floor, image_home_mask)
result = cv2.add(blended_home, blended_floor)

result = result.astype(np.uint8)

cv2.imwrite("outputs/home.jpg", result)
