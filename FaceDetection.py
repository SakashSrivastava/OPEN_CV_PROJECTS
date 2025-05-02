import cv2
face_detect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
webcam=cv2.VideoCapture(0)
while True:
    _,img=webcam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_detect.detectMultiScale(gray,1.1,3)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
    cv2.imshow("Face Detection",img)
    key=cv2.waitKey(10) 
    if key==27: #escape key
        break
webcam.release()
cv2.destroyAllWindows()