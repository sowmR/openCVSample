import cv2
import numpy as np

def empty(arg):
    print("Inside empty function: ", arg)
    pass
windowName = "TrackBars"
# we will introduce track bars to help us manually track the colorswindowName = "TrackBars"
cv2.namedWindow(windowName)
cv2.resizeWindow(windowName,640,240)
'''
First create a HSV tracker
The hue maximum value is 300 in general. But in opencv, it can take only upto 179, which means 180 count.
The saturation and color value will be up to 255
The createTracker function has the following argument
(name oftracker, windowname, minvalue, maxvalue, function to handle the output)
'''
cv2.createTrackbar("hue min",windowName,0,179, empty)
cv2.createTrackbar("hue max",windowName,23,179, empty)
cv2.createTrackbar("sat min",windowName,23,255, empty)
cv2.createTrackbar("sat max",windowName,12,255, empty)
cv2.createTrackbar("val min",windowName,177,255, empty)
cv2.createTrackbar("val max",windowName,21,255, empty)
while True:
    img = cv2.imread("resource/hibiscus500.jpg")
    # detect the yellow color in the image
    img2 = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    # get the values of the trackbar
    h_min = cv2.getTrackbarPos("hue min",windowName) # the name should match the createTracker parameter. it is casesensitive
    h_max = cv2.getTrackbarPos("hue max",windowName)
    s_min = cv2.getTrackbarPos("sat min",windowName)
    s_max = cv2.getTrackbarPos("sat max",windowName)
    v_min = cv2.getTrackbarPos("val min",windowName)
    v_max = cv2.getTrackbarPos("val max",windowName)
    # set the minimum and maximum color values
    lower = np.array([h_min,s_min,v_max])
    upper = np.array([h_max,s_max,v_max])
    # create a mask in the range of the value
    # this will filter out the image with new min and max values.
    mask =cv2.inRange(img2,lower,upper)
    cv2.imshow("image",img2)
    cv2.imshow("masked",mask)
     # break the loop on key press 'q'
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
