import cv2 as cv

img = cv.imread('themes/person2.jpg')
img = cv.resize(img,(500,500))

# Converting the image to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray image",gray)


# How to blur an image
# we are going to use gaussian blur
blur = cv.GaussianBlur(img, (7,7),cv.BORDER_DEFAULT) 
# here (3,3) -> kernel ,should be odd, and decide the quality of the blur
# if it is (7,7) it will be more blur
cv.imshow('Blur image',blur)


# edge cascade -- trying to find the edges that are present in the image
# we are going to use canny edge detector
# it is a multi step process which involves a lot of blurring and then involves a lot of grading computations
cany = cv.Canny(blur,125,175)
# to reduce the amount of edges pass the blur image
cv.imshow("Canny image",cany)


# how to dilate an image using a specific structuring element
dilated = cv.dilate(cany,(3,3),iterations = 1)
cv.imshow("Dilated",dilated)


# eroding the dilated image
eroded = cv.erode(dilated,(3,3),iterations = 1)
cv.imshow("Eroded",eroded)


# resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
# interpolation is useful if u are shrinking the image to dimensions that are smaller than that of the original dimensions
# to enlarge we will use interpolation = cv.INTER_CUBIC
# inter_cubic is slower but the quality is better than inter_linear or inter_area
cv.imshow("Resized",resized)


# Cropping
cropped = img[50:200, 200:400]
cv.imshow("Cropped",cropped)


cv.waitKey(0)