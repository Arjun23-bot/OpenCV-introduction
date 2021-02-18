import cv2
import numpy as np

#requirements
OpenCV --> pip install opencv-python

# Displaying normal color image without a transparent background
#1 = ignore transparency
#-1 = normal color image of the color
#0 = grayscale

img = cv2.imread('C:/Users/paarj/Downloads/hp-omen-17-2019_f2j6.1200.jpg', -1)
img = cv2.resize(img, (0, 0), fx=1.0, fy=1.0 )
img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

