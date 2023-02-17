import cv2 as cv
import numpy as np
import matplotlib as plt

img = cv.imread('themes/person2.jpg')
img = cv.resize(img, (500,500))

# color spaces is basically a space of colors, a system of representing an array of pixel colors
# RGB is a kind of space grayscale is color space.
# We also have other color spaces like HSV, lamb, ....

# BGR to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# BGR to HSV (Hugh Saturation Value) format
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

# BGR to lxaxb / LAB
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("LAB",lab)

# opencv reads images in a BGR format
# openCV displays BGR images
# if we display the same image in another library it follows the RGB format and hence we will see an inversion of colors

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)

# We cannot convert grayscale to HSV directly

# LAB to BGR
lab_bgr = cv.cvtColor(hsv, cv.COLOR_LAB2BGR)
cv.imshow('LAB --> BGR',lab_bgr)

cv.waitKey(0)




