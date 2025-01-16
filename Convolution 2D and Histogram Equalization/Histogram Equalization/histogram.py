import numpy as np
import cv2
import matplotlib.pyplot as plt

def calculate_histogram(image_path):
    
    
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    
    
    image_high_contrast = cv2.equalizeHist(image)
    
   
    hist2 = cv2.calcHist([image_high_contrast], [0], None, [256], [0, 256])


    #Images Plot
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(image, cmap="gray")
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.title('Contrast Image')
    plt.imshow(image_high_contrast, cmap="gray")
    plt.axis('off')

    plt.show()


    #In separated plot
    # plt.figure(figsize=(10, 5))
    # plt.subplot(1, 2, 1)
    # plt.plot(hist, color='r', label='Original Histogram')
    # plt.title('Original Histogram')
    # plt.xlabel('Pixel Value')
    # plt.ylabel('Frequency')
    
    # plt.subplot(1, 2, 2)
    # plt.plot(hist2, color='b', label='Equalized Histogram')
    # plt.title('Equalized Histogram')
    # plt.xlabel('Pixel Value')
    # plt.ylabel('Frequency')
    # plt.tight_layout()
    # plt.show()
   
    #In one plot
    plt.figure(figsize=(10, 5))
    plt.plot(hist, color='r', label='Original Histogram')
    plt.plot(hist2, color='b', label='Equalized Histogram')
    plt.title('Histogram Comparison')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()

    


histogram_image1 = calculate_histogram("Inputs/image1.png")
histogram_image = calculate_histogram("Inputs/image.png")
