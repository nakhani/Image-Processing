import cv2
import numpy as np
import imageio


image = cv2.imread("landscape/6568745aae3f1ce79ce3725f_realistic-winter-photo.png", 0)
image = cv2.resize(image, (420, 380))


frames = []

num_snow = 900
snows= np.random.randint(0, high=420, size=(num_snow, 2))

while True:  
    frame = image.copy()
    
    snows[:, 1] += 3
    
    snows[snows[:, 1] > 300] = np.random.randint(0, high=420, size=(len(snows[snows[:,1] > 300]), 2))
    
    
    for snow in snows:
        cv2.circle(frame, tuple(snow), 1, (156, 200, 245), -1)
       
    
    
    frames.append(frame)


    cv2.imshow("result", frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break




imageio.mimsave('landscape/snowfall.gif', frames)  


