import cv2
import numpy as np


image1 = cv2.imread("")
image2 = cv2.imread("")

image1 = image1.astype(np.float32)
image2 = image2.astype(np.float32)


result = (image1+image2)/2
result = (image1*1/3+image2*2/3)
result = result.astype(np.uint8)


cv2.imwrite("outputs/", result)