import cv2


image = cv2.imread('session26/death_symbol/images.jfif')


diagonal_length = 50  
thickness = 15  

for i in range(diagonal_length):
    for t in range(thickness):
        if i + t < image.shape[1] and diagonal_length - i - 1 + t < image.shape[0]:
            image[diagonal_length - i - 1 + t, i] = [0, 0, 0]  
            image[diagonal_length - i - 1, i + t] = [0, 0, 0]  
        if i - t >= 0 and diagonal_length - i - 1 - t >= 0:
            image[diagonal_length - i - 1 - t, i] = [0, 0, 0]  
            image[diagonal_length - i - 1, i - t] = [0, 0, 0]  

cv2.imwrite('session26/death_symbol/death_image.jpg', image)

cv2.imshow('Death Image', image)
cv2.waitKey(0)
