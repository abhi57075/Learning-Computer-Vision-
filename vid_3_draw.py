import cv2 as cv
import numpy as np

# creating a blank image
blank = np.zeros((500,500,3), dtype = 'uint8') # uint8 is the datatype of an image, 3 is the number of color channels
cv.imshow("Blank",blank)


# paint the image a certain color
blank[200:300,300:400] = (0,255,0)  # blank[:] -> reference all the pixels
cv.imshow("Painted image",blank)


# draw a rectangle
cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness = 2) # 0,0 -> starting 250,250 -> ending 0,255,0 -> color, thickness = cv.Filled/ thickness = -1 -> will fill the whole rectangle
cv.imshow("Rectangle1",blank)


# draw a circle
cv.circle(blank,(250,250),40,(255,0,0),thickness = 3) # 40 is the radius
cv.imshow("Circle",blank)


# draw a line
cv.line(blank,(0,0),(150,150),(255,0,255),thickness = 3)
cv.imshow("Line",blank)


# how to write text on an image
cv.putText(blank,"Hello",(225,225),cv.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), thickness = 2) # 225,225 is the starting position for the text
cv.imshow("Text",blank)


cv.imshow("Image",blank)
cv.waitKey(0)

# there are 2 ways we can draw on images
# 1. By actually drawing on standalone images
# 2. we can create a dummy image or a blank image to work with