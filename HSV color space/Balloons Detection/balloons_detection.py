import cv2
import numpy as np

def detect_balloons(image_path):
    
    image = cv2.imread(image_path)

 
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    #
    lower_hue = np.array([160, 0, 0]) 
    upper_hue = np.array([180, 255, 255])  

   
    mask = cv2.inRange(hsv_image, lower_hue, upper_hue)

  

    
    result = cv2.bitwise_and(image, image, mask=mask)


    cv2.imshow("Original Image", image)
    cv2.imshow("Masked Image", result)
    cv2.imwrite("result.png", result)
    

    cv2.waitKey(0)



detect_balloons('image.png')
