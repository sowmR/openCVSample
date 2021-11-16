import cv2
import matplotlib.pyplot as plt

def getContours(img):
    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(imgray,127,255,0)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        M = cv2.moments(cnt)
        print (M)
        # for this point, we will get the centroid of that contour
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        # get the contour area
        area = cv2.contourArea(cnt)
        # get the contour perimeter
        perimeter = cv2.arcLength(cnt,True)
    img = cv2.drawContours(imgray, contours, -1, (0,255,0),8)
    return img
# load image
img = cv2.imread("resource/shapes.png")
img = cv2.resize(img,(500,500))

rImg = getContours(img)

images =[rImg]
titles=["Contour"]
# View images
col = 3
if len(images)>col:
    row = round(len(images)/col)
else:
    row = 1
for i in range(len(images)):
    plt.subplot(row,col,i+1)
    plt.imshow(images[i], cmap='gray', vmin=0, vmax=255)
    plt.title(titles[i])
plt.show()
