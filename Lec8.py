# shapes and contours

# shape detection

import cv2
import numpy as np



def getContours(img):

    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) # cv2.RETR_ETERNAL -> it gives us the extreme outer contours; cv2.CHAIN_APPROX_NONE -> give us all the contours without any compression
    
    # 1) Contours is a Python list of all the contours/edges/points in the image. 
    # Each individual contour is a Numpy array of (x,y) coordinates of boundary points of the object.4
    # 2) Hierarchy is the parent-child relationship in contours. 
    # It is represented as an array of four values : [Next contour, previous contour, First child contour, Parent contour]

    for cnt in contours:

        area = cv2.contourArea(cnt)
        
        if area > 100 :

            cv2.drawContours(imgContour, cnt, -1, (255,0,0), 3) # -1 means we want to draw all the contours

            peri = cv2.arcLength(cnt, True) # the shape is closed hence true
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True) # we are going to find corner points we have, 0.02*peri is the resolution, True because the shape is closed
            # len(approx) will give us the corner point
            objCor = len(approx)
            x,y,w,h = cv2.boundingRect(approx)

           
            if objCor == 3:
                objectType = "Triangle"
            elif objCor == 4:
                aspRatio1 = w/h
                aspRatio2 = h/w
                if aspRatio1 > 0.80 and aspRatio2 > 0.80:
                    objectType = "Square"
                elif aspRatio1 > 0.80:
                    objectType = "Rectangle"
            else:
                objectType = "Circle"
            
            cv2.rectangle(imgContour, (x,y), (x+w, y+h), (0,0,255), 2)
            cv2.putText(imgContour, objectType, (x+(w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,255), 2)



img = cv2.imread("themes/circle.jpeg")
img = cv2.resize(img,(750,500))

imgContour = img.copy()

imgCanny = cv2.Canny(img, 50, 50)
cv2.imshow("Canny image",imgCanny)

getContours(imgCanny)

cv2.imshow("Image Contour",imgContour)

cv2.waitKey(0) 