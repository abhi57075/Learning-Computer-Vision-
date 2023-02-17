import cv2 as cv
import numpy as np

img = cv.imread('themes/person.jpg')

def rescaleFrame(frame, scale = 0.2):
    # already existing video
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)

    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)

img = rescaleFrame(img)

# Averaging
# We define a kernel window over a specific portion of an image, this window will essentially compute the pixel intensity of the middle pixel of the true center as the average of the surrounding pixel intensities
avg = cv.blur(img, (3,3))
cv.imshow('Average blur',avg) # here 3 by 3 is the size of the kernel

# Gaussian blur
# here same thing happens as that of averaging, but here each pixel is given a particular weight and essentially the product of those weights gives the value for the true center
# we get less blurring as compared to the averaging method
# But the gaussian blur is more natural as compared to averaging
gauss = cv.GaussianBlur(img, (3,3), 0) # 0 here is standard deviation in x direction
cv.imshow("Gausssian blur",gauss)

# Median blur
# same as avg but instead of finding the avg it finds the median of the surrounding pixels
median = cv.medianBlur(img, 3) # here just passing 3, the python compiler will assume the kernel of 3x3 size
cv.imshow("Median blur",median)

# Bilateral blurring - the most effective one
# used in a lot of advanced computer vision projects essentially because of how it blurs
# bilateral blurring applies blurring but retains edges in the images. {most of the blurring techniques do not take this into consideration}
bilateral = cv.bilateralFilter(img,3,15,50) # here 3 is the diameter size, 15 is the sigma color (a larger value for this sigma color means that there are more colors in the neighbourhood that will be considered when the blur is computed), 50 -> sigma space means that pixels further out from the central pixel will influence the blurring calculation
cv.imshow("bilateral blur",bilateral)

cv.waitKey(0)