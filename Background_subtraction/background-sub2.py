# from tkinter import Frame
import cv2 as cv
import numpy as np

def rescaleFrame( frame, scale = 0.2):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)

cap = cv.VideoCapture("E:\\openCV\\videos\\pexels-kelly-lacy-6595761.mp4")

# openCV built-in function for backgournd subtraction-------------------------
subtractor = cv.createBackgroundSubtractorMOG2(history=25, varThreshold=10, detectShadows=True)
while True:
    _, frame = cap.read()
    rescale_frame = rescaleFrame(frame)
    mask = subtractor.apply(rescale_frame)
    cv.imshow("Video", rescale_frame)
    cv.imshow("Mask", mask)
    if cv.waitKey(1) & 0XFF== ord('d'):
        break
 
cap.release()
cv.destroyAllWindows()