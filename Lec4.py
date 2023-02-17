# Shapes and texts

import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8) # since 0 represents black color, 3 represents the color channel
cv2.imshow("Black image",img)
print(img.shape)



# coloring the whole image to blue
img[:] = 255,0,0
# cv2.imshow("Blue image",img)



# drawing a line
cv2.line(img,(0,0),(250,250),(0,0,255),3) # (0,0) is the starting point; (250,250) is the end point; (0,0,255) is the colour; 3 is the thickness
cv2.line(img,(img.shape[0],0),(0,img.shape[0]),(0,255,0),3)



# drawing a rectangle
cv2.rectangle(img, (img.shape[0],img.shape[1]), (200,200), (255,255,0), -1) # -1 thickness means that the rectangle will be coloured



# drawing a circle
cv2.circle(img, (250,250), 40, (255,155,155), 10) # (250,250) -> center 40 is the radius



# put text on images
cv2.putText(img, "CREATIVE", (50,100), cv2.FONT_HERSHEY_COMPLEX, 2 ,(100,100,255), 5) # (50,100) is the start position, 10 is the scale


cv2.imshow("IMAGE",img)


cv2.waitKey(0)