import cv2


image = cv2.imread('cat_counter/cat.png')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalcatface.xml')


faces = face_detector.detectMultiScale(image_gray)

num_cats = len(faces)
print(f'Number of cats detected: {num_cats}')
cv2.putText(image, f'Number of cats detected: {num_cats}', (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2, cv2.LINE_AA)


for face in faces:
    x, y, w, h = face
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

cv2.imshow('Cat Number', image)
cv2.waitKey(0)
