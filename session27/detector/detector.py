import cv2
import numpy as np

lower_gray = 46
upper_gray = 220

lower_white = 200
upper_white = 255

lower_black = 0
upper_black = 45


cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('detector/output.mp4', fourcc, 20.0, (640, 480))


while True:
    _, frame = cap.read()


    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    contrast_frame = cv2.equalizeHist(gray_frame)

  

    new_gray_frame = cv2.cvtColor(contrast_frame, cv2.COLOR_GRAY2BGR)

    height, width, _ = frame.shape

    rect_width, rect_height = 100, 100
    rect_x = width // 2 - rect_width // 2
    rect_y = height // 2 - rect_height // 2
    
    
    blurred_frame = cv2.GaussianBlur(new_gray_frame, (51, 51), 20)

    blurred_frame[rect_y:rect_y + rect_height, rect_x:rect_x + rect_width] = new_gray_frame[rect_y:rect_y + rect_height, rect_x:rect_x + rect_width]

 
    point = contrast_frame[rect_y:rect_y + rect_height, rect_x:rect_x + rect_width]
    

    mask_gray = cv2.inRange(point, lower_gray, upper_gray)
    mask_white = cv2.inRange(point, lower_white, upper_white)
    mask_black = cv2.inRange(point, lower_black, upper_black)

    if np.sum(mask_gray) > np.sum(mask_white) and np.sum(mask_gray) > np.sum(mask_black):
        color = "Gray"
    elif np.sum(mask_white) > np.sum(mask_gray) and np.sum(mask_white) > np.sum(mask_black):
        color = "White"
    else:
        color = "Black"

    cv2.rectangle(blurred_frame, (rect_x, rect_y), (rect_x + rect_width, rect_y + rect_height), (0, 0, 0), 2)
    cv2.putText(blurred_frame, color, (rect_x, rect_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 0), 2, cv2.LINE_AA)


    out.write(blurred_frame)
    cv2.imshow("Detector", blurred_frame)

   
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break


