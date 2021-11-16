import cv2

img = cv2.imread('resource/hibiscus500.jpg')
print(img.shape)
# the above print will return (width, height, channel)
# 3 = BGR

imgR = cv2.resize(img,(1000,1000))
print(imgR.shape)
cv2.imshow("image",imgR)
cv2.waitKey(2000)