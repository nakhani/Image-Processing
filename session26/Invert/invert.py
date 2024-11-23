import cv2

image1 = cv2.imread('session26/Invert/1.jpg')
inverted_image1 = cv2.bitwise_not(image1)
cv2.imwrite('session26/Invert/inverted_image1.jpg', inverted_image1)

image2 = cv2.imread('session26/Invert/2.jpg')
inverted_image2 = cv2.bitwise_not(image2)
cv2.imwrite('session26/Invert/inverted_image2.jpg', inverted_image2)

cv2.imshow('Original Image 1', image1)
cv2.imshow('Inverted Image 1', inverted_image1)
cv2.imshow('Original Image 2', image2)
cv2.imshow('Inverted Image 2', inverted_image2)
cv2.waitKey(0)

