import cv2
import numpy as np

def non_square_sticker(frame, face_detector, sticker):
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(frame_gray, 1.3, 5)
    for face in faces:
        x, y, w, h = face
        sticker_resized = cv2.resize(sticker, (w, int(w * sticker.shape[0] / sticker.shape[1])))
        for c in range(0, 3):
            frame[y:y+sticker_resized.shape[0], x:x+sticker_resized.shape[1], c] = sticker_resized[:,:,c] * (sticker_resized[:,:,3]/255.0) + frame[y:y+sticker_resized.shape[0], x:x+sticker_resized.shape[1], c] * (1.0 - sticker_resized[:,:,3]/255.0)
    return frame

def stickers_on_eyes_and_lips(frame, face_detector, eye_detector, mouth_detector, eye_sticker , lip_sticker):
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(frame_gray, 1.3, 5)
    for face in faces:
        x, y, w, h = face
        face_gray = frame_gray[y:y+h, x:x+w]
        face_color = frame[y:y+h, x:x+w]
        
        eyes = eye_detector.detectMultiScale(face_gray, 1.1, 5)
        if len(eyes) >= 2:
            eye1= eyes[0]
            if len(eyes) > 1:
              eye2= eyes[1]  
            else:
                None
            if eye2 is not None and eye2[0] < eye1[0]:
                eye1, eye2 = eye2, eye1

            ex1, ey1, ew1, eh1 = eye1 
            if eye2 is not None:
             ex2, ey2, ew2, eh2 = eye2 

            else:
                eye1 

            eye_center = ((ex1 + ex2 + ew1) // 2, (ey1 + ey2 + eh1) // 2)
            if eye2 is not None:
              glasses_width = 2 * abs(ex2 + ew2 - ex1)
            else:
                2 * ew1  
            glasses_height = int(glasses_width * eye_sticker.shape[0] / eye_sticker.shape[1])

            glasses_resized = cv2.resize(eye_sticker, (glasses_width, glasses_height))

            y1 = max(0, eye_center[1] - glasses_height // 2) 
            y2 = y1 + glasses_height 
            x1 = max(0, eye_center[0] - glasses_width // 2) 
            x2 = x1 + glasses_width

            y2 = min(face_color.shape[0], y2) 
            x2 = min(face_color.shape[1], x2) 
            
            h, w = y2 - y1, x2 - x1 
            glasses_resized = cv2.resize(glasses_resized, (w, h)) 
            for c in range(0, 3): 
              face_color[y1:y2, x1:x2, c] = glasses_resized[:,:,c] * (glasses_resized[:,:,3] / 255.0) + face_color[y1:y2, x1:x2, c] * (1.0 - glasses_resized[:,:,3] / 255.0)

        mouths = mouth_detector.detectMultiScale(face_gray, 1.8, 5) 
        for mouth in mouths: 
            mx, my, mw, mh = mouth 
            if mw > 0 and mh > 0: 
              lip_sticker_resized = cv2.resize(lip_sticker, (mw, mh)) 
              for c in range(0, 3): 
                  face_color[my:my+mh, mx:mx+mw, c] = lip_sticker_resized[:,:,c] * (lip_sticker_resized[:,:,3]/255.0) + face_color[my:my+mh, mx:mx+mw, c] * (1.0 - lip_sticker_resized[:,:,3]/255.0)
    return frame



def chess_face(frame, face_detector):
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(frame_gray, 1.3, 5)
    for face in faces:
        x, y, w, h = face
        face_frame = frame[y:y+h, x:x+w]
        face_frame_small = cv2.resize(face_frame, (10, 10))
        face_frame_big = cv2.resize(face_frame_small, (w, h), interpolation=cv2.INTER_NEAREST)
        frame[y:y+h, x:x+w] = face_frame_big
    return frame

def mirror_filter(frame):
    flipped_frame = cv2.flip(frame, 1)
    half_width = frame.shape[1] // 2 
    original_resized = cv2.resize(frame, (half_width, frame.shape[0])) 
    flipped_resized = cv2.resize(flipped_frame, (half_width, frame.shape[0])) 
    combined_frame = np.hstack((original_resized, flipped_resized)) 
    return combined_frame

cap = cv2.VideoCapture(0)
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
mouth_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")

sticker = cv2.imread('face_filter/photos/PngItem_1361499.png', -1)
eye_sticker = cv2.imread('face_filter/photos/eye.png', -1)
lip_sticker = cv2.imread('face_filter/photos/lips.png', -1)

current_filter = None

while True:
    _, frame = cap.read()

    key = cv2.waitKey(1) & 0xFF
    if key == ord('1'):
        current_filter = 'non_square_sticker'
    elif key == ord('2'):
        current_filter = 'stickers_on_eyes_and_lips'
    elif key == ord('3'):
        current_filter = 'chess_face'
    elif key == ord('4'):
        current_filter = 'mirror_filter'
    elif key == ord('q'):
        break

    if current_filter == 'non_square_sticker':
        frame = non_square_sticker(frame, face_detector, sticker)
    elif current_filter == 'stickers_on_eyes_and_lips':
        frame = stickers_on_eyes_and_lips(frame, face_detector, eye_detector, mouth_detector, eye_sticker, lip_sticker)
    elif current_filter == 'chess_face':
        frame = chess_face(frame, face_detector)
    elif current_filter == 'mirror_filter':
        frame = mirror_filter(frame)

    cv2.imshow("result", frame)


