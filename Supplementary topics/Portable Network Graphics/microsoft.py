import cv2
import numpy as np

def create_logo():

    height, width = 450, 1000
    
    red_channel = np.full((height, width), 88, dtype=np.uint8)
    green_channel = np.full((height, width), 84, dtype=np.uint8)
    blue_channel = np.full((height, width), 84, dtype=np.uint8)
    alpha_channel = np.full((height, width), 0, dtype=np.uint8)  
    
    shape_info = [
        ((150, 220), (150, 220), (242, 80, 34)),    
        ((150, 220), (230, 300), (127, 186, 0)),    
        ((230, 300), (150, 220), (0, 164, 239)),   
        ((230, 300), (230, 300), (255, 185, 0)),    
    ]
    
    for (y1, y2), (x1, x2), (r, g, b) in shape_info:
        red_channel[y1:y2, x1:x2] = r
        green_channel[y1:y2, x1:x2] = g
        blue_channel[y1:y2, x1:x2] = b
        alpha_channel[y1:y2, x1:x2] = 255  
    

    logo_image = cv2.merge([blue_channel, green_channel, red_channel, alpha_channel])
    
   
    cv2.putText(logo_image, 'Microsoft', (340, 255), cv2.FONT_HERSHEY_TRIPLEX, 3.7, (255, 255, 255, 255), 5, cv2.LINE_AA)
    
    
    cv2.imwrite('result.png', logo_image)
    
  
    cv2.imshow("result", logo_image)
    cv2.waitKey(0)
    

create_logo()
