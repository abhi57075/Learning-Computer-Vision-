import cv2 as cv
import numpy as np

img = cv.imread('themes/person2.jpg')
img = cv.resize(img, (500,500))


# translation is basically shifting the image along x or y axis

def translate(img,x,y): # x and y here stands for the number of pixels u want to shift along x or y axis
    # to translate an image we need to create a translation matrix
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[0],img.shape[1])
    return cv.warpAffine(img, transMat, dimensions)

# -x -> left
# -y -> up
# +x -> right
# +y -> down

translated = translate(img,100,100)
cv.imshow("Translated",translated)

# Rotation

def rotate(img, angle, rotPoint = None):
    (height,width) = img.shape[:2] # [:2] of the first two values

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0) # 1.0 is the scale
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

# clockwise -> -ve
# counter clockwise -> +ve

rotated = rotate(img,45)
cv.imshow("Rotated",rotated)

# resizing
# shrinking = INTER_AREA
# enlarging = INTER_LINEAR/ INTER_CUBIC
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow("Resized",resized)

# flipping
# 0 means flipping the image over x axis/ vertically
# 1 means flipping the image over y axis/ horizontally
# -1 means flipping the image in both x and y axis

flip = cv.flip(img, 0)
cv.imshow("flip",flip)

cv.waitKey(0)