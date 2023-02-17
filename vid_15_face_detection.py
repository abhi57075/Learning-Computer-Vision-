# detecting faces using har cascade
# face detection is performed using classifiers
# a classifier is essentially an algorithm that decides whether a given image is positive or negative, whether a face is present or not
# Now classifier needs to be trained on 1000s of images with and without faces
# opencv comes with a lot of pre trained classifiers that we can use in any program
# so essentially the two main classifiers that exist today are har cascades and more advanced classifiers - core local binary patterns 

# Face detection does not involve skin tone or the colors that are present in the image.
# These haar cascades essentially look at an object in an image and using the edges tries to determine whether it is a face or not

import cv2 as cv
import numpy as np

img = cv.imread('themes/person2.jpg')

def rescaleFrame(frame, scale = 0.2):
    # already existing video
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)

    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)

img = rescaleFrame(img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Person',gray)

haar_cascade = cv.CascadeClassifier("haar_face.xml")

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 1) # minNeighbors is a parameter that specifies the number of neighbours a rectangle should have to be called a face
# returns the rectangular co ordinates of the face as a list to faces_rect

print(len(faces_rect))

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness = 2)

cv.imshow("Detected Faces",img)

cv.waitKey(0)

# you will see that har cascades are really sensitive to noise in an image
# one way to minimize this error is by decreasing the minimum neighbors
# har cascades are not the most effective in detecting faces but they are popular

# If we want to extend this to videos we will have to detect har cascades on each individual frame of the video