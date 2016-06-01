import cv
import time

cv.NamedWindow("camera", 1)
capture = cv.CreateCameraCapture(0)

width = None #leave None for auto-detection
height = None #leave None for auto-detection

if width is None:
    width = int(cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_WIDTH))
else:
	cv.SetCaptureProperty(capture,cv.CV_CAP_PROP_FRAME_WIDTH,width)    

if height is None:
	height = int(cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_HEIGHT))
else:
	cv.SetCaptureProperty(capture,cv.CV_CAP_PROP_FRAME_HEIGHT,height) 

result = cv.CreateImage((width,height),cv.IPL_DEPTH_8U,3)

while True:
    img = cv.QueryFrame(capture)
    cv.Smooth(img,result,cv.CV_GAUSSIAN,9,9)
    #cv.Dilate(img,result,None,5) #uncommet to apply affect
    #cv.Erode(img,result,None,1) #uncommet to apply affect
    #cv.Smooth(img,result,cv.CV_GAUSSIAN) #uncommet to apply affect
    cv.ShowImage("camera", result)
    k = cv.WaitKey(10);
    if k == 'f':
        break
