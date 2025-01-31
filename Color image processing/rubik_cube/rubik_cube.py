import cv2 


image = cv2.imread('image (1).png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

blue_channel, red_channel, green_channel= cv2.split(image)


for i, row in enumerate(zip(red_channel, green_channel, blue_channel)):
    r_val, g_val, b_val = row
    for j, pixel in enumerate(zip(r_val, g_val, b_val)):
        if pixel == (0, 255, 255): 
            image[i, j] = [255, 0, 0] 
        elif pixel == (255, 0, 255):  
            image[i, j] = [0, 255, 0]  
        elif pixel == (0, 0, 255):  
            image[i, j] = [255, 255, 0]  



image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
cv2.imwrite('result.png', image)
