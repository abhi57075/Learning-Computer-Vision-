import cv2
import os
from cvzone.HandTrackingModule import HandDetector
import numpy as np
from PIL import Image,ImageTk

data_dir = ("themes")
path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]

for image in path:
    img = Image.open(image)
    cv2.imshow("images",img)

cv2.waitKey(0)