import cv2


def contour_area(contour):
    
    n = len(contour)
    if n < 3:  
        return 0

    area = 0
    for i in range(n):
        x1, y1 = contour[i][0]
        x2, y2 = contour[(i + 1) % n][0]
        area += x1 * y2 - x2 * y1
        area = abs(area) * 0.5

    return area


image = cv2.imread('image.png')
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, binary_image = cv2.threshold(grayscale, 127, 255, cv2.THRESH_BINARY)


contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

contour_area_list= []


for contour in contours:
    area = contour_area(contour)
    contour_area_list.append(area)


#for area, coords in contour_area_list:
#   print(f"Contour Area: {area}, Coordinates: {coords}")

print(len(contour_area_list))

