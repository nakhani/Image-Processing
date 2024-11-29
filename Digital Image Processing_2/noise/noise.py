import cv2
import numpy as np
import imageio

image = cv2.imread("noise/Samsung-Lifestyle-TV-The-Sero-05-2.jpg", 0)
image = cv2.resize(image, (400,250))

x_black, y_black, w_black, h_black = 80, 49, 248, 148
 
image[y_black:y_black+h_black, x_black:x_black+w_black]= 0

x, y, w, h = 84, 53, 240, 140

frames =[]
while True:
        frame = np.random.random((h,w))*255
        frame = np.array(frame, dtype=np.uint8)

        new_image =image.copy()
        new_image[y:y+h, x:x+w]= frame
        frames.append(new_image)

        cv2.imshow("result",new_image)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break


imageio.mimsave('noise/tv_noise.gif', frames)