import cv2
import numpy as np

# First lets create a matrix of 0s
# img = np.zeros((500,500)) # black and white
img = np.zeros((512,512,3),np.uint8) # color/ grayscale
# img[:] = 255,0,0 # color the whole image
# img[200:300,100:200] = 23,27,88 # color only certain part of the image.

# cv2.line(img,(0,0),(200,200),(0,23,255),3) # (image,startingpoint, endingpoint, color, thickness)
# cv2.rectangle(img,(0,0),(200,200),(255,27,255),2) # rectangle outline
# cv2.rectangle(img,(10,10),(200,100),(255,67,186),cv2.FILLED) # filled rectangle

# cv2.circle(img,(400,50),30,(255,34,217),5) # circle outline - (image, center point, radius, color, thickness)

cv2.putText(img,"Open CV Text",(100,200),cv2.FONT_HERSHEY_COMPLEX,2,(0,130,12),1) # (image,textToOverlay, startingpoint, fontface,fontscale,color, thickness)

cv2.imshow("image",img)
cv2.waitKey(2000)