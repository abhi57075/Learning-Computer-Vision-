# Warp perspective

# ek image lets say a card -> heart of king
# yeh image thodi tilted hai
# iss tilted image ko hume ekdum seedha karna hai
# so for this we use warp perspective

# to find the exact location of the edges of the card
# open the image in paint
# hover around the edges and you will see its co ordinates


import cv2
import numpy as np

kernel = np.ones((5,5), np.uint8)


img = cv2.imread("themes/cards.jpeg")
cv2.imshow("Cards",img)


width,height = 250, 350


pts1 = np.float32([[341,81],[646,133],[268,524],[578,572]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]]) # here we are defining that [341,81] is the left most point or the 1st edge and [578,572] is the last edge and so on...


matrix = cv2.getPerspectiveTransform(pts1,pts2)


imgOutput = cv2.warpPerspective(img, matrix, (width,height))


cv2.imshow("Warp Image",imgOutput)


cv2.waitKey(0)