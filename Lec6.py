# Joining images

import cv2
import numpy as np

img1 = cv2.imread("themes/abstract.jpeg")
img2 = cv2.imread("themes/cards.jpeg")

img1 = cv2.resize(img1,(500,500))
img2 = cv2.resize(img2,(700,500)) # for horizontal stack only the height should be same
# img3 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

imgHor = np.hstack((img1,img2))
cv2.imshow("Horizintal Stack",imgHor)


imgHor = cv2.resize(imgHor, (200,200))
cv2.imshow("resized horizontal stack", imgHor)


img1 = cv2.resize(img1,(500,700))
img2 = cv2.resize(img2,(500,500))

imgVer = np.vstack((img1,img2))
cv2.imshow("Vertical Stack",imgVer)

# there are some issues with this method
# There is no option of resizing the image
# will give an error if the images do not have the same number of channels

cv2.waitKey(0)
