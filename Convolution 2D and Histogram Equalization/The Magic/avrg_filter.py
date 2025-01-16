import numpy as np
import cv2
import matplotlib.pyplot as plt

def avrg_filter(image_path):
    
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    
    filters = {
        "Avg_kernel 5x5: 0.04": np.ones((5, 5), np.float32) /25,
        "Avg_kernel 5x5: 1.0": np.ones((5, 5), np.float32) ,
        "Avg_kernel 5x5: 5.0": np.ones((5, 5), np.float32) * 5.0 ,
        "Avg_kernel 3x3: 0.04": np.ones((3, 3), np.float32) /25,
        "Avg_kernel 3x3: 1.0": np.ones((3, 3), np.float32) ,
        "Avg_kernel 3x3: 5.0": np.ones((3, 3), np.float32) * 5.0 
    }
    
    
    filtered_images = [("Original", image)]

    
    for filter_name, kernel in filters.items():
        filtered_image = cv2.filter2D(image, -1, kernel)
        filtered_images.append((filter_name, filtered_image))

    
    plt.figure(figsize=(20, 10))
    for i, (title, img) in enumerate(filtered_images):
        plt.subplot(1, len(filtered_images), i + 1)
        plt.imshow(img, cmap='gray')
        plt.title(title)
        plt.axis('on')

    plt.tight_layout()
    plt.show()
    


image = avrg_filter("1.png")
