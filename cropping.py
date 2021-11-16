import cv2

img = cv2.imread('resource/hibiscus500.jpg')
# image can be considered as array of pixels. to crop, we will just provide the actual pixel range.

imgC = img[0:200,200:500] # [height, width]
cv2.imshow("Image",imgC)
cv2.waitKey(2000)