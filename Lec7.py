# Color Detection

import cv2
import numpy as np

path = "themes/person2.jpg"
img = cv2.imread(path)
img = cv2.resize(img,(500,300))



def empty(a):
    pass



cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,250)

cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty) # We will be putting this trackbar on "Trackbar" Windows, 0 is the initial value
# Hue has max value of 360 but in opencv we have its max value as 179 that is total 180 values
# Every time the user changes its value the empty function will be called
cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty) # the initial values are obtained by trial and error
cv2.createTrackbar("Sat Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Value Min", "TrackBars", 60, 255, empty)
cv2.createTrackbar("Value Max", "TrackBars", 255, 255, empty)



while True :

    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # Hue Saturation Value
    imgHSV = cv2.resize(imgHSV,(500,300))

    hue_min = cv2.getTrackbarPos("Hue Min","TrackBars")
    hue_max = cv2.getTrackbarPos("Hue Max","TrackBars")
    sat_min = cv2.getTrackbarPos("Sat Min","TrackBars")
    sat_max = cv2.getTrackbarPos("Sat Max","TrackBars")
    value_min = cv2.getTrackbarPos("Value Min","TrackBars")
    value_max = cv2.getTrackbarPos("Value Max","TrackBars")

    print(hue_min,hue_max,sat_min,sat_max,value_min,value_max)

    lower = np.array([hue_min,sat_min,value_min])
    upper = np.array([hue_max,sat_max,value_max])
    masked = cv2.inRange(imgHSV,lower,upper)

    #The cv2.inRange function expects three arguments: the first is the image were we are going to perform color detection, 
    #the second is the lower limit of the color you want to detect, 
    #and the third argument is the upper limit of the color you want to detect.

    imgResult = cv2.bitwise_and(imgHSV,imgHSV, mask = masked)

    cv2.imshow("Original",img)
    cv2.imshow("IMAGE HSV",imgHSV)
    cv2.imshow("Mask Image",masked)
    cv2.imshow("Masked output",imgResult)

    cv2.waitKey(1)