# STEPS :
# 1. Reading the web frames
# 2. Creating the findColor function
# 3. Now for each of the masks that we have detected where is the object - for that we will use contours

import cv2
import numpy as np

frameWidth = 650
frameHeight = 450

cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,130) # Increase the brightness to 130

myColors = [[79,60,186,113,192,255],
            [0,142,102,179,255,255]] # hue min, sat min, value min, hue max, sat max, value max

myColorValues = [[255,0,0],[0,0,255]] # Blue and red

myPoints = [] # [x, y, colorID]

def findColor(img,myColors, myColorValues):

    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # Hue Saturation Value

    # color_list = ["BLUE","GREEN","RED"]

    count = 0
    # index = 0

    newPoints = []

    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        masked = cv2.inRange(imgHSV,lower,upper)
        masked = cv2.resize(masked,(650,450))

        
        x,y = getContours(masked)
        cv2.circle(imgResult,(x,y),5,myColorValues[count],cv2.FILLED)
        # cv2.imshow(f"{color_list[index]} MASKED ",masked)
        # index += 1

        if x!=0 and y!=0:
            newPoints.append([x,y,count])

        count+=1
    return newPoints

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) # cv2.RETR_ETERNAL -> it gives us the extreme outer contours; cv2.CHAIN_APPROX_NONE -> give us all the contours without any compression
    x,y,w,h = 0,0,0,0
    
    for cnt in contours:
        area = cv2.contourArea(cnt)
        
        if area > 500 :
            # cv2.drawContours(imgResult, cnt, -1, (255,0,0), 3) # -1 means we want to draw all the contours
            peri = cv2.arcLength(cnt, True) # the shape is closed hence true
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True) # we are going to find corner points we have, 0.02*peri is the resolution, True because the shape is closed
            x,y,w,h = cv2.boundingRect(approx)
    
    return x+w//2, y # it will return the position for our writing

def drawOnCanvas (myPoints, myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], -1)

while True :

    success, img = cap.read()

    imgResult = img.copy()

    newPoints = findColor(img,myColors,myColorValues)

    if len(newPoints)!=0:
        for newP in newPoints:
            myPoints.append(newP)
    
    if len(myPoints)!=0:
        drawOnCanvas(myPoints,myColorValues)

    cv2.imshow("Original",img)
    cv2.imshow("Final Image",imgResult)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break