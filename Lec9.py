# Face Detection

import cv2

img = cv2.imread("themes/faces2.jpeg")
img = cv2.resize(img, (500,350))

faceCascade = cv2.CascadeClassifier("haar_face.xml")

# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(img, 1.1, 4) # 1.1 is the scale factor, 4 is the min neighbors
print(faces)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)



cv2.imshow("Result",img)
cv2.waitKey(0)