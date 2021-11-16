import cv2
''' Comment/ unComment each section as needed'''
# print(cv2.__version__)

'''
Read Image
'''
# img = cv2.imread('./resource/hibiscus.jpg')
# cv2.imshow("output",img)  
# cv2.waitKey(0)

'''
Read Video from file
'''
# vcap = cv2.VideoCapture('./resource/testVideo.mp4')
# while True:
#     success, img = vcap.read()
#     cv2.imshow("Video",img)
#     # break the loop on key press 'q'
#     if cv2.waitKey(1) & 0xFF==ord('q'):
#         break

'''
capture video from the webcam
0 => default video device connected to the pc.
If there is more than one camera device, device id is passed as parameter.

For the set function, the arguments are (propertyID, value)
refer to https://docs.opencv.org/4.5.3/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d 
for the list of properties available. We can give the name of the property or the indexID of the list
'''

vcap = cv2.VideoCapture(0)
vcap.set(3,640) # 3= width
vcap.set(4,480) # 4 = height
vcap.set(10,20) # 10 = brightness
vcap.set(11,20) # 11 = contrast
vcap.set(12,20) # 12 = saturation
while True:
    success, img = vcap.read()
    cv2.imshow("Video",img)
    # break the loop on key press 'q'
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
