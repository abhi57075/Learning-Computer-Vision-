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

# Thresholding is binarization of an image
# In general we want to take an image and convert it to a binary image that is an image where pixels are either 0 or black or 255 or white
# if the pixel intensity of the image is less than the threshold value we set that pixel intensity to zero. And if it is above this threshold value we set it to 255 or white

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY) # 150 is the threshold value, if the pixel intensity is greater than 150 we set it to 245
cv.imshow("Simple threshold",thresh)

# Inverse thresholding
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV) # 150 is the threshold value, if the pixel intensity is greater than 150 we set it to 245
cv.imshow("Simple threshold",thresh_inv)

# Adaptive thresholding
# We let the computer find the optimal threshold value by itself
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3) # 255 is the maximum value, 11 is the kernel size, 3 (which is c) is subtracted from the mean allowing us to essentially fine tune our threshold
cv.imshow("adaptive thresholding",adaptive_thresh)

adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3) # 255 is the maximum value, 11 is the kernel size, 3 (which is c) is subtracted from the mean allowing us to essentially fine tune our threshold
cv.imshow("adaptive thresholding",adaptive_thresh)


cv.waitKey(0)