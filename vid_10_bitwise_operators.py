import cv2 as cv
import numpy as np

# A pixel is turned off it has a value of zero and is turned on if it has a value of 1

blank = np.zeros((400,400),dtype = "uint8")

rectangle = cv.rectangle(blank.copy(), (30,30),(370,370), 255, -1) # 255 is the color and -1 means fill completely
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1) # 200,200 is the center and 200 is the radius

# cv.imshow("Rectangle",rectangle)
# cv.imshow("Circle",circle)

# Bitwise AND -> intersecting regions
bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow("bitwise and",bitwise_and)

# Bitwise OR -> non intersecting and intersecting regions
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow("bitwise or",bitwise_or)

# Bitwise XOR -> non intersecting regions
bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow("bitwise xor",bitwise_xor)

# Bitwise NOT 
# Bitwise AND
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow("bitwise not",bitwise_not)

cv.waitKey(0)