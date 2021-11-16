import cv2
import numpy as np

img = cv2.imread("resource/hibiscus500.jpg")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# horStack = np.hstack((img,img))
# verStack = np.vstack((img,img))

'''
The disadvantage of the above method are
- The images cannot be resized
- if two images are of difference channels (eg: one is gray and other is color), it will not work.
'''
# function to handle resize to two different image size
# resource: https://github.com/murtazahassan/Learn-OpenCV-in-3-hours/blob/master/chapter6.py
def stackImages (size,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, size, size)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, size, size)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, size, size)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,size, size)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

verStack = stackImages(0.5,([img,imgGray,img],[img,img,img]))
cv2.imshow("Image", verStack)
cv2.waitKey(5000)