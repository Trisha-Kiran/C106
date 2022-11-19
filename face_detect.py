import cv2

img = cv2.imread("4f.jpg")

gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

faces = face_cascade.detectMultiScale(gray,1.1,3)
print(len(faces))

for (x,y,w,h) in faces:
     cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
     face1 = img[y:y+h,x:x+h]
     cv2.imwrite("face1.jpg",face1)
             
cv2.imshow('img',img)
cv2.waitKey(0)


