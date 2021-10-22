# Introduction

Install openCV into your environment using the link below
[https://docs.opencv.org/master/da/df6/tutorial_py_table_of_contents_setup.html]

## Import

``` import cv2```

here,  cv = computer vision

## read images Videos and webcam

image can be read using the function 

```image =  cv2.imread(filename)```

The read image can be viewed using the function

```cv2.imshow(windowName,image)```

It is good to add wait statement after the imshow, so that we can view the image. otherwise, the window will open and close right away.

```cv2.waitkey(millliseconds)```

if milliseconds=0, it will wait for infinite amount of time. the window will be only by clicking the close button on the window.