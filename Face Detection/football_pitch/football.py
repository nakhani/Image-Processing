import cv2


background = cv2.imread('football_pitch/istockphoto-1208398773-612x612.jpg')
background = cv2.resize(background, (900, 600))


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

