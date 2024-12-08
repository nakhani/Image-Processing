import cv2



image1= cv2.imread("inputs/text2.jpg",-1)
image2= cv2.imread("inputs/text1.jpg",-1)


#result = image1 -image2
result = cv2.subtract(image1, image2)
result2 = 255-result


cv2.imwrite("outputs/text2.jpg", result2)