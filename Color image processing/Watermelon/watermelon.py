import cv2


def create_materwelon(image_path):
    
    image = cv2.imread(image_path)
    
    
    blue_channel, green_channel, red_channel = cv2.split(image)
    
    merged_image = cv2.merge((blue_channel, red_channel, green_channel))
    
    cv2.imwrite('materwelon.jpg', merged_image)
    cv2.imshow('materwelon', merged_image)
    cv2.waitKey(0)
    

image_path = 'image.png'
create_materwelon(image_path)
