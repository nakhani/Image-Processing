import cv2
import numpy as np

image1 = cv2.imread("inputs/face1.webp")
image2 = cv2.imread("inputs/face2.webp")

image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

image1 = image1.astype(np.float32)
image2 = image2.astype(np.float32)

nums = 5

images = []

for i in range(nums + 1):
    alpha = i / nums
    result = (1 - alpha) * image1 + alpha * image2
    result = result.astype(np.uint8)
    images.append(result)
    #cv2.imwrite(f"outputs/morphing_{i}.jpg", result)

final_result = np.concatenate(images, axis=1)

cv2.imwrite("outputs/Morphing.jpg", final_result)
