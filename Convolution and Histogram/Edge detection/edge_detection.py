import numpy as np
import cv2
import matplotlib.pyplot as plt

def edge_detection(image_path):

   

    image_color = cv2.imread(image_path)
    image_gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    rows, cols = image_gray.shape
    result = np.zeros((rows, cols), dtype=np.uint8)

    
    kernel = np.array([[-1, -1, -1],
                       [-1,  8, -1],
                       [-1, -1, -1]])

  
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            small = image_gray[i-1:i+2, j-1:j+2] 
            edge_value = np.sum(kernel * small) 
            result[i, j] = np.clip(edge_value, 0, 255)  

  
    
    

    
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title('Original Color Image')
    plt.imshow(cv2.cvtColor(image_color, cv2.COLOR_BGR2RGB)) 
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title('Edge Detection Result')
    plt.imshow(result, cmap='gray')
    plt.axis('off')

    plt.show()


image_1 = edge_detection("image.jpg")
image_2 = edge_detection("image-_1_.jpg")