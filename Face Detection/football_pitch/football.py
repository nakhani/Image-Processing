import cv2
import numpy as np

background = np.ones((600, 897, 3), dtype=np.uint8)

light_green = (64, 128, 0)
dark_green = (34, 139, 34)

for i in range(7):
    if i % 2 == 1:
     color = light_green  
    else:
      color = dark_green

    x_start = i * 128
    x_end = x_start + 128
    cv2.rectangle(background, (x_start, 0), (x_end, 600), color, -1)


white = (255, 255, 255)

cv2.rectangle(background, (50, 50), (850, 550), white, 5)

cv2.line(background, (450, 50), (450, 550), white, 5)

cv2.circle(background, (450, 300), 70, white, 5)

cv2.circle(background, (450, 300), 8, white, -1)

cv2.rectangle(background, (50, 200), (150, 400), white, 5)
cv2.rectangle(background, (750, 200), (850, 400), white, 5)

cv2.rectangle(background, (50, 250), (100, 350), white, 5)
cv2.rectangle(background, (800, 250), (850, 350), white, 5)



cv2.imshow('Football Pitch', background)
cv2.waitKey(0)

