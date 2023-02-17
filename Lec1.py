import cv2 # cv stands for computer vision

# Read images, videos and webcam

# Reading and displaying the image
img = cv2.imread('themes/abstract.jpeg')
cv2.imshow("Output Image",img)



# How to use webcam
cap = cv2.VideoCapture(0)
# We want our webcam to be of a specific size
cap.set(3,640) # width is 3 and we are setting it to 640
cap.set(4,480) # height is 4 and we are setting it to 480
cap.set(10, 100) # 10 is the id for brightness 

while True:
    success, img = cap.read()
    cv2.imshow("Webcam", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 
# cv2.waitKey(0) # 0 means infinite delay and if lets say 1 then wait for 1 millisecond



# Reading and displaying the video
cap = cv2.VideoCapture('Videos/video1.mp4')
# We know that video is just a sequence of images
while True:
    success, img = cap.read() # the frame will be saved in img and success variable will tell us whether this process was done successfully or not i.e it will be a boolean variable
    cv2.imshow("Video Output",img)
    if cv2.waitKey(1) & 0xFF == ord('q'): # when the key 'q' is pressed on the keyboard there will be a delay of 1ms and the video will stop playing
        break 
    
cv2.waitKey(0)

