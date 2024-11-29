import cv2


image = cv2.imread("")

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face_detector = cv2.CascadeClassifier("")

faces = face_detector.detectMultiScale(image_gray)

for face in faces:
    x, y, w, h = face
    cv2.rectangle(image_gray, ())



cv2.imshow("result", faces)
cv2.waitKey(0)