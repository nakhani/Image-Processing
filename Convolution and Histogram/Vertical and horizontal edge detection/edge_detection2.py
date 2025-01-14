import numpy as np
import cv2
import matplotlib.pyplot as plt

def edge_detection(image_path):
   
    
    image_color = cv2.imread(image_path)
    image_gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
  
    rows, cols = image_gray.shape

    
    kernel_vertical = np.array([[-1, 0, 1],
                                [-2, 0, 2],
                                [-1, 0, 1]])

    kernel_horizontal = np.array([[1, 2, 1],
                                  [0, 0, 0],
                                  [-1, -2, -1]])

    
    result_v = np.zeros((rows, cols), dtype=np.uint8)
    result_h = np.zeros((rows, cols), dtype=np.uint8)


    for i in range(1, rows-1):
        for j in range(1, cols-1):
            region = image_gray[i-1:i+2, j-1:j+2]
            edge_v = np.sum(kernel_vertical * region)
            result_v[i, j] = np.clip(edge_v, 0, 255)

    for i in range(1, rows-1):
        for j in range(1, cols-1):
            region = image_gray[i-1:i+2, j-1:j+2]
            edge_h = np.sum(kernel_horizontal * region)
            result_h[i, j] = np.clip(edge_h, 0, 255)


    plt.figure(figsize=(12, 6))
    plt.subplot(1, 3, 1)
    plt.title('Original Color Image')
    plt.imshow(cv2.cvtColor(image_color, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.title('Vertical Edges')
    plt.imshow(result_v, cmap='gray')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.title('Horizontal Edges')
    plt.imshow(result_h, cmap='gray')
    plt.axis('off')

    plt.show()

image = edge_detection("image.png")