# In this code we will perform the basic background by using the diff function -----
# diff function is a pre-defined function

import cv2 as cv
import numpy as np

def rescaleFrame(frame, scale= 0.2):
    width = int(frame.shape[1]* scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)

cap = cv.VideoCapture("videos\pexels-kelly-lacy-9318006.mp4")

_, first_f = cap.read()
scale_img = rescaleFrame(first_f)
thrash = cv.cvtColor(scale_img, cv.COLOR_BGR2GRAY)
frame_blur = cv.GaussianBlur(thrash, (1,1), 0)

cv.imshow("1st Frame", frame_blur)
while True:
    _, f = cap.read()
    resizedFrame = rescaleFrame(f)
    gray = cv.cvtColor(resizedFrame, cv.COLOR_BGR2GRAY)
    blur_cap = cv.GaussianBlur(gray, (1,1), 0)
    cv.imshow("Frame", blur_cap)

    # Taking the difference of the frames and the scale_img ------------------------
    diff = cv.absdiff(frame_blur, blur_cap)
    _, difference = cv.threshold(diff, 25, 255, cv.THRESH_BINARY)
    cv.imshow("Frame Difference", difference)

    if cv.waitKey(1) & 0xFF==ord('d'):
        break
cap.release()
cv.destroyAllWindows()


cv.waitKey(0)