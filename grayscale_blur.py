import cv2

img = cv2.imread("resource/hibiscus500.jpg")

# # convert the image to gray scale
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow("gray Image",imgGray)
# cv2.waitKey(2000)

# blur the image.
# Gaussian blur parameters are
# 1 - image
# 2 - kernel size (radius, width) - it should be odd numbers
# 3 - sigmaX - set to 0 for now.
imgBlur = cv2.GaussianBlur(img,(9,7), 0)
cv2.imshow("original Image",img)
cv2.imshow("blur image",imgBlur)
cv2.waitKey(2000)