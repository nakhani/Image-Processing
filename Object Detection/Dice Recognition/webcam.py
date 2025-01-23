import cv2 as cv

def funny_webcam(image_path):
    image_original = cv.imread(image_path)
    cap = cv.VideoCapture(0)

 
    image_height, image_width = image_original.shape[:2]

    
    w = image_width // 3
    h = image_height // 3

    while True:
        ret, frame = cap.read()
        if not ret:
            break

       
        center_y, center_x = frame.shape[:2]
        center_x = (center_x - w) // 2
        center_y = (center_y - h) // 2

       
        image = image_original.copy()

        
        image[image_height//2 - h//2:image_height//2 + h//2, image_width//2 - w//2:image_width//2 + w//2] = frame[center_y:center_y + h, center_x:center_x + w]

        cv.imshow('Webcam', image)
        if cv.waitKey(25) & 0xFF: 
            break

    cap.release()
    cv.destroyAllWindows()


funny_webcam('inputs/img.png')
