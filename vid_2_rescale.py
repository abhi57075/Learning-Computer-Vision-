import cv2 as cv
import numpy as np

img = cv.imread('themes/person2.jpg') # this will return the image as matrix of pixels

resized_image = cv.resize(img, (500,500))
cv.imshow("Resized Image",resized_image)

capture = cv.VideoCapture("Videos/video1.mp4") # now we will pass 0,1,2 or 3 if we wanna use webcam

while True:
    isTrue, frame = capture.read()

    frame_resized = cv.resize(frame, (500,500))

    cv.imshow("Video Resized", frame_resized)

    if cv.waitKey(20) & 0xFF == ord('q'): # if the letter d is pressed then break out of this loop
        break

cv.waitKey(0)

capture.release()
cv.destroyAllWindows()