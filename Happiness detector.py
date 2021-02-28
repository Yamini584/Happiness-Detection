import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade=cv2.CascadeClassifier('haarcascade_smile.xml')
#0 for webcam of computer and 1 for eternal device webcam
webcam = cv2.VideoCapture(0)

while True:
    check, frame = webcam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     #faces are tuples of four elements
    faces = face_cascade.detectMultiScale(frame,1.1,5)
    for x,y,w,h in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 3)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray,1.1,22)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,0), 2)
        smiles = smile_cascade.detectMultiScale(roi_gray,2.0,50)
        for (sx,sy,sw,sh) in smiles:
            cv2.rectangle(roi_color, (sx,sy), (sx+sw, sy+sh), (0,0,255), 2)
    cv2.imshow('Face Detector', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
webcam.release()
cv2.destroyAllWindows()

