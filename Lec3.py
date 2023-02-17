# Resizing and cropping

import cv2
import numpy as np

kernel = np.ones((5,5), np.uint8) # uint8 means the value can range from 0 to 255

img = cv2.imread("themes/abstract.jpeg")



# to find size of the image
print(img.shape) # this will give the answer as (w,h,c); h is for height, w is for width, c is for channel



# Resize
imgResize = cv2.resize(img,(750,500)) # 750 is the width and 500 is the height
cv2.imshow("Resized image",imgResize)
print(imgResize.shape)



# Cropping an image
imgCropped = imgResize[100:200,50:300] # here 100:200 is the width and 50:300 is the height
cv2.imshow("Cropped image", imgCropped)




cv2.waitKey(0)