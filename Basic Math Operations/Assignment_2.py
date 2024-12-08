import os 
import numpy as np
import cv2

def delete_noise(folder_path):
    image_files = os.listdir(folder_path)
    images = []

    for image_file in image_files:
        image = cv2.imread(os.path.join(folder_path, image_file), cv2.IMREAD_COLOR)
        image = image.astype(np.float32)
        images.append(image)

    result = np.zeros_like(images[0])
    for image in images:
        result += image

    result /= len(images)
    result = result.astype(np.uint8)

    return result

folder_1 = delete_noise("inputs/blackhole/1")
folder_2 = delete_noise("inputs/blackhole/2")
folder_3 = delete_noise("inputs/blackhole/3")
folder_4 = delete_noise("inputs/blackhole/4")

left_right_top = cv2.hconcat([folder_1, folder_2])
left_right_bottom = cv2.hconcat([folder_3, folder_4])

result = cv2.vconcat([left_right_top, left_right_bottom])

cv2.imwrite("outputs/black_hole.jpg", result)
