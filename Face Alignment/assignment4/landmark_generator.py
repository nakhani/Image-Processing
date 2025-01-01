import numpy as np
import cv2
import tensorflow as tf
from functools import partial
import time
from TFLiteFaceDetector import UltraLightFaceDetecion
from TFLiteFaceAlignment import CoordinateAlignmentModel


fd = UltraLightFaceDetecion("weights/RFB-320.tflite", conf_threshold=0.88)
fa = CoordinateAlignmentModel("weights/coor_2d106.tflite")

image = cv2.imread("input/person.jpg") 
color = (0, 0, 255)



start_time = time.perf_counter()

boxes, scores = fd.inference(image)

for pred in fa.get_landmarks(image, boxes):
    for i,p in enumerate(np.round(pred).astype(np.int16)):
                cv2.circle(image, tuple(p), 1, color, 1)
                cv2.putText(image, str(i), tuple(p), cv2.QT_FONT_NORMAL ,0.25, (0,255,0),0)


print(time.perf_counter() - start_time)

cv2.imshow("result", image)
cv2.waitKey()
cv2.imwrite("output/result1.jpg", image)
         
