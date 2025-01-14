import numpy as np
import cv2
import matplotlib.pyplot as plt

def mean_filtering(image_path):
    
    
    image = cv2.imread(image_path)
   
    
    kernel_sizes = [3, 5, 15]
    
   
    results = {}
    for k in kernel_sizes:
        kernel = np.ones((k, k), np.float32) / (k * k)
        result = cv2.filter2D(image, -1, kernel)
        results[k] = result
       


    plt.figure(figsize=(15, 10))
    plt.subplot(2, 2, 1)
    plt.title('Original Color Image')
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    for i, k in enumerate(kernel_sizes, 2):
        plt.subplot(2, 2, i)
        plt.title(f'Mean Filtering {k}x{k}')
        plt.imshow(cv2.cvtColor(results[k], cv2.COLOR_BGR2RGB))
        plt.axis('off')

    plt.show()

image = mean_filtering("image.png")
image_1 = mean_filtering("image1.jpg")
image_2 = mean_filtering("image2.jpg")