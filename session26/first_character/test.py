import cv2

width, height = 400, 400


image = cv2.imread('session26/first_character/black-image.jpg', 0)
image = cv2.resize(image,(width,height))
image = cv2.bitwise_not(image)


color = (0, 0, 0) 
square_size = 40  


cv2.rectangle(image, (40, 40), (40 + square_size, 40 + 8 * square_size), color, -1)  
cv2.rectangle(image, (40 + square_size, 40), (40 + 2 * square_size, 40 + square_size), color, -1)  # Top horizontal part of the diagonal
#cv2.rectangle(image, (60 + 7 * square_size, 60 + 7 * square_size), (60 + 8 * square_size, 60 + 8 * square_size), color, -1)  # Bottom horizontal part of the diagonal
#cv2.rectangle(image, (60 + 8 * square_size, 60), (60 + 9 * square_size, 60 + 8 * square_size), color, -1)  # Right vertical line

# Display the image with the letter "N"
cv2.imshow('Pixelated N', image)
cv2.imwrite("session26/first_character/pixelated_N.jpg", image)
cv2.waitKey(0)

