import cv2 

def detect_mouth(image):
    
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    mouth_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

   
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

   
    faces = face_cascade.detectMultiScale(gray_image, 1.3, 5)
    
    
    mouth_box = None

    for (x, y, w, h) in faces:
        
        roi_gray = gray_image[y:y + h, x:x + w]
        roi_color = image[y:y + h, x:x + w]

        
        mouths = mouth_cascade.detectMultiScale(roi_gray, 1.3, 5)

        for (mx, my, mw, mh) in mouths:
           
            if my > h // 2:
                mouth_box = (x + mx, y + my, mw, mh)
                break

    return mouth_box

def funny_webcam(image_path, zoom_factor):
    image_original = cv2.imread(image_path)
    cap = cv2.VideoCapture(0)

    mouth_box = detect_mouth(image_original)
    if mouth_box is None:
        print("No mouth detected in the image.")
        return

    x, y, w, h = mouth_box

    
    w_zoomed = int(w * zoom_factor)
    h_zoomed = int(h * zoom_factor)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        center_y, center_x = frame.shape[:2]
        center_x = (center_x - w_zoomed) // 2
        center_y = (center_y - h_zoomed) // 2

        cropped_frame = frame[center_y:center_y + h_zoomed, center_x:center_x + w_zoomed]
        cropped_frame_resized = cv2.resize(cropped_frame, (w, h))

        image = image_original.copy()
        image[y:y + h, x:x + w] = cropped_frame_resized

        cv2.imshow('Webcam', image)
        if cv2.waitKey(25) & 0xFF == 27:  
            break

   


funny_webcam('image.png', zoom_factor=2.5)
