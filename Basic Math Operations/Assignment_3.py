import cv2

image = cv2.imread("inputs/person.jpg", 0)

inverted = 255-image

blurred = cv2.GaussianBlur(inverted, (21,21), 0)

epsilon = 1e-5

inverted_blurred = (255-blurred) + epsilon

sketch = image/inverted_blurred
sketch_white = sketch * 255
sketch_black = sketch_white - 255

cv2.imwrite("outputs/sketch1.jpg", sketch_white)
cv2.imwrite("outputs/sketch2.jpg", sketch_black)