import cv2


def rotate_image(image, angle):
    
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    
    return rotated


image = cv2.imread('image.jpg')


rotated_image = rotate_image(image, 180)

cv2.imshow('rotated image', rotated_image)
cv2.waitKey()
\

cv2.imwrite('rotated_image.jpg', rotated_image)
