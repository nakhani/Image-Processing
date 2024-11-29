import cv2

image = cv2.imread('session26/Rotate/3.jpg')
image = cv2.resize(image,(400,280))

rotated_image = cv2.rotate(image, cv2.ROTATE_180)

cv2.imwrite('session26/Rotate/rotated_image.jpg', rotated_image)

cv2.imshow('Original Image', image)
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
