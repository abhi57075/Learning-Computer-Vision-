import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('themes/person.jpg')

def rescaleFrame(frame, scale = 0.2):
    # already existing video
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)

    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)

img = rescaleFrame(img)

# histograms allows us to visualize the distribution of pixel intensities in an image
# if its a color image or a greyscale image we can visualize these pixel intensity distribution with the help of a histogram

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# grayscale histogram

gray_hist = cv.calcHist([gray], [0], None, [256], [0,256]) # 256 is the number of bins. [0,256] is the range of all the pixel values

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel("Bins")
plt.ylabel("No of pixels")
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

cv.waitKey(0)

# Color histogram

blank = np.zeros(img.shape[:2], dtype = 'uint8')

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

masked = cv.bitwise_and(img,img,mask = mask)
cv.imshow("mask",mask) 

plt.figure()
plt.title('Colour Histogram')
plt.xlabel('Bins')
plt.ylabel("no of pixels")

colors = ('b','g','r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist, color = col)
    plt.xlim([0,256])

plt.show()