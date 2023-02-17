# Basic functions

import cv2
import numpy as np

kernel = np.ones((5,5), np.uint8) # uint8 means the value can range from 0 to 255

img = cv2.imread("themes/abstract.jpeg")

# img = cv2.resize(img, (500,500), interpolation = cv2.INTER_AREA) or we can write
img = cv2.resize(img, (500,500))
cv2.imshow("Resized Image",img)




# Converting the image to grayscale

# In openCV the channels are BGR (blue, green, red)
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # cvtColor converts the image to various color spaces
cv2.imshow("Gray Image",grayImg)



# Blurring the image

# We will be using the Gaussian blur function to blur our image
# We could use either the colored image or the gray image
imgBlur = cv2.GaussianBlur(grayImg, (7,7), 1)  # (7,7) is the kernel size and it should be of an odd number, 0 is the sigma x {A kernel is like a matrix}
cv2.imshow("Blur Image", imgBlur)



# Edge Detector (Canny edge Detector)

imgCanny = cv2.Canny(img, 100, 100) # 100, 100 are the 2 threshold values
cv2.imshow("Canny Image",imgCanny)



# Image Dilation

# Sometimes we are detecing an edge but because there is a gap or it is not joined properly it does not detect it as a proper line
# So we will increase the thickness of our edge
imgDilation = cv2.dilate(imgCanny, kernel, iterations = 1) # how many iterations we want the kernel to move around/ how much thickness do we actually need
cv2.imshow("Dilated Image", imgDilation) 



#  Erosion (Opposite of dilation)

imgEroded = cv2.erode(imgDilation, kernel, iterations = 1)
cv2.imshow("Eroded Image",imgEroded)



cv2.waitKey(0)