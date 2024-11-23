import cv2


width, height = 400, 400

image = cv2.imread("session26/first_character/black-image.jpg", 0)
image = cv2.resize(image, (width,height))
image = cv2.bitwise_not(image)


color = (0, 0, 0)  
thickness = 30


start_point1 = (100, 300) 
end_point1 = (100, 100)   
cv2.line(image, start_point1, end_point1, color, thickness, lineType=cv2.LINE_AA)

start_point2 = (100, 100)  
end_point2 = (300, 300)    
cv2.line(image, start_point2, end_point2, color, thickness, lineType=cv2.LINE_AA)

start_point3 = (300, 300)  
end_point3 = (300, 100)    
cv2.line(image, start_point3, end_point3, color, thickness, lineType=cv2.LINE_AA)


cv2.imshow('Letter N', image)
cv2.imwrite("session26/first_character/letter_N.jpg", image)
cv2.waitKey(0)

