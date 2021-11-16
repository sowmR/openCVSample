import cv2
import numpy as np
img = cv2.imread('resource/cards1.jpg')
# got the points manually by opening the image in paint.
points = [
    [348,281],
    [806,114],
    [781,765],
    [1284,532]
]
width,height = 250,350
pts1 = np.float32(points)
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOp = cv2.warpPerspective(img, matrix,(width,height))
cv2.imshow("image",imgOp)
cv2.waitKey(5000)