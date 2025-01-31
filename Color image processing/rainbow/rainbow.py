import cv2
import numpy as np

def draw_rainbow():
    height, width = 400, 800
    
    red_channel = np.zeros((height, width), dtype=np.uint8)
    green_channel = np.zeros((height, width), dtype=np.uint8)
    blue_channel = np.zeros((height, width), dtype=np.uint8)
    
    radius = 300
    thickness = 30
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    
    center_x, center_y = width // 2, height - 400

    for color in colors:
        if color == 'red':
            cv2.ellipse(red_channel, (center_x, center_y), (radius, radius), 0, 0, 180, 255, thickness)
        elif color == 'orange':
            cv2.ellipse(red_channel, (center_x, center_y), (radius, radius), 0, 0, 180, 128, thickness)
            cv2.ellipse(green_channel, (center_x, center_y), (radius, radius), 0, 0, 180, 128, thickness)
        elif color == 'yellow':
            cv2.ellipse(red_channel, (center_x, center_y), (radius, radius), 0, 0, 180, 255, thickness)
            cv2.ellipse(green_channel, (center_x, center_y), (radius, radius), 0, 0, 180, 255, thickness)
        elif color == 'green':
            cv2.ellipse(green_channel, (center_x, center_y), (radius, radius), 0, 0, 180, 255, thickness)
        elif color == 'blue':
            cv2.ellipse(blue_channel, (center_x, center_y), (radius, radius), 0, 0, 180, 255, thickness)
        elif color == 'indigo':
            cv2.ellipse(blue_channel, (center_x, center_y), (radius, radius), 0, 0, 180, 128, thickness)
            cv2.ellipse(red_channel, (center_x, center_y), (radius, radius), 0, 0, 180, 64, thickness)
        elif color == 'violet':
            cv2.ellipse(blue_channel, (center_x, center_y), (radius, radius), 0, 0, 180, 255, thickness)
            cv2.ellipse(red_channel, (center_x, center_y), (radius, radius), 0, 0, 180, 128, thickness)

        radius -= thickness

    rainbow_image = cv2.merge((blue_channel, green_channel, red_channel))
    rainbow_image = cv2.rotate(rainbow_image, cv2.ROTATE_180)
    
    cv2.imwrite('rainbow_image.png', rainbow_image)
 

    return 'rainbow_image.png'

def final_rainbow(image_path):
   
    rainbow_image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    
    
    white_background = np.ones_like(rainbow_image) * 255
    
    
    mask = cv2.cvtColor(rainbow_image, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(mask, 26, 255, cv2.THRESH_BINARY)
    mask = cv2.merge([mask, mask, mask])

  
    result = np.where(mask == 255, rainbow_image, white_background)


    cv2.imwrite('final_rainbow.png', result)
    cv2.imshow('Rainbow', result)
    cv2.waitKey(0)
    


image_path = draw_rainbow()


final_rainbow(image_path)
