import cv2 as cv
import numpy as np

img = cv.imread('themes/person2.jpg')
img = cv.resize(img, (500,500))

# A color image basically consists of multiple channels, red, green and blue

b,g,r = cv.split(img)
cv.imshow('Blue',b)
cv.imshow("Green",g)
cv.imshow("Red",r)

print(img.shape) # 3 represents 3 color channels blue, green, red
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow("Merged image",merged)

blank = np.zeros(img.shape[:2], dtype = 'uint8')

blue = cv.imshow([b,blank,blank])
green = cv.imshow([blank,g,blank])
red = cv.imshow([blank,blank,r])
cv.imshow('Blue',blue)
cv.imshow("Green",green)
cv.imshow("Red",red)

cv.waitKey(0)
