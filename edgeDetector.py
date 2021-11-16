import cv2
import numpy as np

img = cv2.imread('resource/hibiscus500.jpg')
kernel = np.ones((5,5),np.uint8)

# change the threshold value to see the change in the edge lines detections.
imgcanny = cv2.Canny(img, 200,150)
# increase the thickness of the edges
imgDilation = cv2.dilate(imgcanny,kernel,iterations = 5)
# decrease the thickness of the edges
imgErode = cv2.erode(imgDilation,kernel, iterations = 4)

cv2.imshow("Edge detection",imgErode)
cv2.waitKey(2000)
