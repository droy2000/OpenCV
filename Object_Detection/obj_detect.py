import cv2 as cv

# import numpy as np

def rescaleFrame(frame, scale = 0.3):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

cap = cv.VideoCapture("videos\Pexels_Videos_2103099.mp4")

# cap.set(cv.CAP_PROP_FPS, 20)
fps = cap.get(cv.CAP_PROP_FPS)
print("fps:", fps)

# For writing the video back to the file---------------------------------------------------------

 

# Object detection from stable camera

object_detection = cv.createBackgroundSubtractorMOG2(history=200, varThreshold=40)

print(cap.isOpened())


while cap.isOpened():
    ret, ori = cap.read()
    frame = rescaleFrame(ori)

    height, width, _ = frame.shape
    print(height, width)

    # ROI 
    roi = frame[130:648, 120:1100]
    cv.imshow('ROI', roi)

    # Object Detection code -----------------------------------------------------------------------------------------
    mask = object_detection.apply(roi)
    contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    for cnt in contours:

        # calculate area and remove small elements
        area = cv.contourArea(cnt)
        if area > 100:
            # cv.drawContours(roi, [cnt], -1, (0, 255, 0), 1)
            x,y,w,h = cv.boundingRect(cnt)
            cv.rectangle(roi, (x,y), (x+w, y+h), (0, 255, 0), 2)

 
    cv.imshow('Mask', mask)
    # out.write(frame)
    cv.imshow("Frame", frame)
    out.write(frame)
    if cv.waitKey(2) & 0xFF== ord('d'):
        break
                  
    

cap.release()
out.release()

cv.destroyAllWindows()
cv.waitKey(0)


