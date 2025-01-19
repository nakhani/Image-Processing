import cv2
import numpy as np



def find_contours(binary_image):
    contours = []
    
    height, width = binary_image.shape
    store_pixel = np.zeros((height, width), dtype=bool)

    def check_pixel(x,y):
        return 0 <= x < width and 0 <= y < height and binary_image[y, x] > 0 and not store_pixel[y, x]
    
    def extract_contour(x_start, y_start):
        contour = []
        stack = [(x_start, y_start)]
        
        while stack:
            x, y = stack.pop()
            if check_pixel(x,y) :
                store_pixel[y, x] = True
                contour.append((x, y))
                for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1), (x-1, y-1), (x-1, y+1), (x+1, y-1), (x+1, y+1)]:
                    if check_pixel(nx,ny):
                        stack.append((nx, ny))
        return contour
    
    for y in range(height):
        for x in range(width):
            if check_pixel(x,y):
                contour = extract_contour(x, y)
                if contour:
                    contours.append(contour)
    
    return contours



    
image = cv2.imread('image.png')

grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, binary_image = cv2.threshold(grayscale, 127, 255, cv2.THRESH_BINARY)
    
contours = find_contours(binary_image)

print(len(contours))
#print(contours)


