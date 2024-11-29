import cv2

width, height = 400, 300


gradient_image = cv2.imread('session26/Gradient/black-image.jpg', cv2.IMREAD_COLOR)
gradient_image = cv2.resize(gradient_image,(width,height))


for x in range(height):
    color_value = 255 - int((x / height) * 255)  
    cv2.line(gradient_image, (0, x), (width, x), (color_value, color_value, color_value), 1)


cv2.imshow('Gradient', gradient_image)
cv2.imwrite("session26/Gradient/gradient.jpg", gradient_image)
cv2.waitKey(0)
