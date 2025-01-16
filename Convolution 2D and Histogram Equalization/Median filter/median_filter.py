import cv2
import numpy as np
import matplotlib.pyplot as plt

def median_filter(image_path):

   

    image = cv2.imread(image_path)


    # rows, cols = image.shape
    # result = np.zeros((rows, cols), dtype=np.uint8)

    
    # for i in range(1, rows-1):
    #     for j in range(1, cols-1):
    #         small = image[i-1:i+2, j-1:j+2] 
    #         sorted_array = np.sort(small, axis=None) 
    #         result[i, j] = sorted_array[4]


    #result= cv2.medianBlur(image, 5)
    
    result= cv2.medianBlur(image, 3)
    result= cv2.medianBlur(result, 3)
    
   
   
   

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title('Original Color Image')
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)) 
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title('Noise Reduction Result')
    plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    plt.show()



image_1 = median_filter("Inputs/image.png")
image_2 = median_filter("Inputs/image1.png")
image_3 = median_filter("Inputs/image 2.png")
image_4 = median_filter("Inputs/image-3.png")
image_5 = median_filter("Inputs/image 4.png")
image_6 = median_filter("Inputs/image-5.png")