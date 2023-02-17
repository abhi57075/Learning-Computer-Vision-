import cv2 as cv
import numpy as np

img = cv.imread('themes/cards.jpg')

def rescaleFrame(frame, scale = 0.2):
    # already existing video
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)

    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)

img = rescaleFrame(img)

# Gradient and edges are completely different from a mathematical point of view but from a programming perspective they are kind of same thing only

# we have done the canny edge detection method

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# 1. Laplacian edge detection method
lap = cv.Laplacian(gray, cv.CV_64F) # cv.64F is the data depth
lap = np.uint8(np.absolute(lap))
cv.imshow("Laplacian",lap)
# when we transition from black to white and white to black that is considered a positive and a negative slope. 
# Now images itself cannot have negative pixel values
# So what we do is we essentially compute the absolute value of that image.
# So all the pixel values of the image are converted to the absolute values.
# and then we convert that to a UI 28 to an image specific data type

# 2. Sobel gradient magnitude representation
# sobel computes the gradient in two directions x and y
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0) # x dir is 1 and y dir is 0
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1) # x dir is 0 and y dir is 1
cv.imshow('Sobel X', sobelx)
cv.imshow("Sobel Y", sobely)

combined_sobel = cv.bitwise_or(sobelx,sobely)
cv.imshow("Combined Sobel",combined_sobel)

# Canny method 
canny = cv.Canny(gray, 150, 175)
cv.imshow("Canny",canny)


cv.waitKey(0)