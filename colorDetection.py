import cv2
import numpy as np

img = cv2.imread("resource/hibiscus2.jpg")
# convert the image to HSV color space
hsvImg = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# define the range of yellow
yellow_high = np.array([63,90,100]) # HSV
yellow_low = np.array([11,88,73]) # HSV
 # Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsvImg, yellow_low, yellow_high)

# Bitwise-AND mask and original image
res = cv2.bitwise_and(img,img, mask= mask)

# display the image
cv2.imshow('original',img)
# cv2.imshow('hsv',hsvImg)
# cv2.imshow('mask',mask)
cv2.imshow('res',res)
cv2.waitKey(0)
cv2.destroyAllWindows() 