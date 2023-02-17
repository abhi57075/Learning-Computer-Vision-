import cv2 as cv
import numpy as np

img = cv.imread('themes/person2.jpg')
img = cv.resize(img, (500,500))

# contours are basically the boundaries of objects
# from mathematical point of view contours and edges are different 
# contours are useful tools when we get into shape analysis and object detection and recognition

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

canny = cv.Canny(img,125,175)

# we will use the find Contour method
# it basically returns 2 things contours and hierarchies

# cv.RETR_TREE -> if we want all the hierarchial contours
# cv.RETR_EXTERNAL -> if we want only the external contours
# cv.RETR_LIST -> if we want all the contours in the image

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST,cv.CHAIN_APPROX_NONE)

# here contours will be essentially a python list of all the coordinates of the contours that were in the image
# hierarchies -> it refers to the hierarchial representation of contours
# lets ay we have a line
# cv.CHAIN_APPROX_NONE -> will return all the contours of the points of the line
# cv.CHAIN_APPROX_SIMPLE -> will return only the starting and end point contour of the line (which makes more sense)

print(len(contours))

# another way of finding contours instead of using canny edge detector is threshold
# threshold looks at an image and tries to binarize the image

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY) # if the intensity/density of the pixel is below 125 it is going to be set to zero
cv.imshow("Thresh",thresh)
print(len(thresh))

blank = np.zeros(img.shape,dtype = 'uint8')
# cv.imshow("Blank",blank)

cv.drawContours(blank,contours,-1,(0,0,255),1) # -1 means we want all the contours in our image, 2 is the thickness
cv.imshow("Contours drawn", blank)

cv.waitKey(0)
