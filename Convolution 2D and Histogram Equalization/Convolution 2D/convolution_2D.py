import numpy as np
import cv2
import matplotlib.pyplot as plt



def Convolution_2D(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    filters = {
        "Edge Detection": np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]),
        "Sharpening": np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]),
        "Emboss": np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]]),
        "Identity": np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]]),
        "Vertical Detection": np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
    }

    plt.figure(figsize=(15, 10))

    for filter_name, kernel in filters.items():
        filtered_image = cv2.filter2D(image, -1, kernel)
        result = np.hstack((image, filtered_image))

        plt.imshow(result, cmap='gray')
        plt.title(filter_name)
        plt.axis('off')

        plt.show()
    
    return result

result_image = Convolution_2D("image.jpg")
