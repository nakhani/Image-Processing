import cv2


image = cv2.imread('image.png')
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, binary_image = cv2.threshold(grayscale, 127, 255, cv2.THRESH_BINARY)


contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


def bounding_rect(contour):
    x_min = min([point[0][0] for point in contour])
    y_min = min([point[0][1] for point in contour])
    x_max = max([point[0][0] for point in contour])
    y_max = max([point[0][1] for point in contour])
    
    x = x_min
    y = y_min
    w = x_max - x_min
    h = y_max - y_min
    
    return x, y, w, h


bounding_rects = []
for contour in contours:
    x, y, w, h = bounding_rect(contour)
    bounding_rects.append((x, y, w, h))
    print("Bounding Rectangle:", (x, y, w, h))
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)


cv2.imshow('Bounding Rectangles', image)
cv2.waitKey()

