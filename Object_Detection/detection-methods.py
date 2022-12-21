# from turtle import width
import cv2 as cv
import numpy as np
# from object_detection import ObjectDetection

object_detector = cv.createBackgroundSubtractorMOG2(history=200, varThreshold=35)


def rescaleFrame(frame, scale = 0.3):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)
    
cap = cv.VideoCapture("E:\\openCV\\videos\\Pexels_Videos_2103099.mp4")

while True:
    _, video = cap.read()
    rescaled = rescaleFrame(video)
    height, width, _ = rescaled.shape
    print(height, width)

    # Extract region of interest(roi) ---------------------------------------------------
    roi = rescaled[175:648, 100:968]
    cv.imshow('Roi', roi)

    # Apply mask only on the roi-------------------------------------------------------
    mask = object_detector.apply(roi)
    
    # Find the contours in the video----------------------------------
    contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    for i in contours:
        # Calculate area and remove small elements
        area = cv.contourArea(i)
        if area > 200:
            # cv.drawContours(roi,[i], -1, (0, 255, 0), 1)
            x,y,w,h = cv.boundingRect(i)
            cv.rectangle(roi, (x,y), (x+w, y+h), (0,255,0),2)

        

    cv.imshow('Frame', rescaled)
    cv.imshow('Mask', mask)

    if cv.waitKey(1) & 0XFF== ord('d'):
        break
cap.release()
cv.destroyAllWindows