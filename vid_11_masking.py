import cv2 as cv
import numpy as np

img = cv.imread('themes/person2.jpg')
img = cv.resize(img, (750,750))

def rescaleFrame(frame, scale = 0.2):
    # already existing video
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)

    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)

# img = rescaleFrame(img)

# Masking essentially allows us to focus on certain parts of an image that we would like to focus on

blank = np.zeros(img.shape[:2], dtype = 'uint8') # the dimensions of the mask have to be the same size as that of the image
#cv.imshow('Blank Image',blank)

circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1) # here radius is 100 px, 255 is the mask, -1 is the thickness

rectangle = cv.rectangle(blank.copy(), (30,30),(370,370), 255, -1) # 255 is the color and -1 means fill completely

weird_shape = cv.bitwise_and(circle,rectangle)
cv.imshow('Weird shape',weird_shape)

masked = cv.bitwise_or(img,img,mask=weird_shape)
cv.imshow("Weird shaped Masked image",masked)

cv.waitKey(0)