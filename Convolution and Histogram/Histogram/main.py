import numpy as np
import cv2
import matplotlib.pyplot as plt

def calculate_histogram(image_path):
    
    image = cv2.imread(image_path)

    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    histogram = np.zeros(256)

    #height, width = image.shape[:2]

    #for i in range(height): 
    #  for j in range(width): 
    #      pixel = image[i, j] 

    image_flattened = grayscale_image.flatten()

    for pixel in image_flattened:
        histogram[int(pixel)] += 1

    return histogram


image_path = 'plage.jpg'  

histogram = calculate_histogram(image_path)


plt.figure(figsize=(10, 5))
plt.plot(histogram, color='r')
plt.title('Histogram using plt.plot()')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.show()


plt.figure(figsize=(10, 5))
plt.hist(range(256), weights=histogram, bins=256, color='b')
plt.title('Histogram using plt.hist()')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.xticks(np.arange(0, 257, step=50)) 
plt.yticks(np.arange(0, max(histogram)+1, step=5000)) 
plt.show()


plt.figure(figsize=(10, 5))
plt.bar(range(256), histogram, color='g')
plt.title('Histogram using plt.bar()')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.show()
