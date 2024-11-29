import cv2


board_size = 8
square_size = 60


image_width = board_size * square_size
image_height = board_size * square_size


chessboard = cv2.imread('session26/chessboard/black-image.jpg', 0)
chessboard = cv2.resize(chessboard, (image_width, image_height))


for row in range(board_size):
    for col in range(board_size):
        
        if (row + col) % 2 == 0:
            color = (255, 255, 255)  
        else:
            color = (0, 0, 0)  
            
        
       
        start_x = col * square_size
        start_y = row * square_size
        end_x = start_x + square_size
        end_y = start_y + square_size
        
        
        cv2.rectangle(chessboard, (start_x, start_y), (end_x, end_y), color, -1)


cv2.imshow('Chessboard', chessboard)
cv2.imwrite("session26/chessboard/chessboard.jpg", chessboard)
cv2.waitKey()

