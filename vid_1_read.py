import cv2 as cv

# Reading images

# img = cv.imread('themes/person2.jpg') # this will return the image as matrix of pixels
# cv.imshow("Person",img) # this method displays the image as a new window


# Reading videos

capture = cv.VideoCapture("Videos/video1.mp4") # now we will pass 0,1,2 or 3 if we wanna use webcam
# to read a video we read the video frame by frame

while True:
    isTrue, frame = capture.read()

    # capture.read() returns a frame and a boolean that says whether the frame was successfully read in or not
    cv.imshow("Video",frame)

    # to stop the video from playing infinte frames
    if cv.waitKey(20) & 0xFF == ord('q'): # if the letter q is pressed then break out of this loop
        break

cv.waitKey(0)

capture.release()
cv.destroyAllWindows()



# -215:Assertion failed -> it means that open CV could not find a media file at that particular location that you specified

# cv.waitKey(0) # it waits for a specific delay or time in milliseconds for key to be pressed

# Rescaling video implies modifying its height and width to a particular height and width
