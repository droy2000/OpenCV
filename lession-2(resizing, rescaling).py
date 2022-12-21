
from turtle import shape
import cv2 as cv

img = cv.imread('python\cvpython\glass.png')
cv.imshow('glass', img)
#--------------------------------------------------------------------

# for video rescaling --------------------------------------------------

def rescaleFrame(frame, scale=0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# use for image rescaling-------------------------------------------
resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)
cv.waitKey(0)


# use only for live video -------------------------------------------

def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)

#-------------------------------------------------------------------

capture = cv.VideoCapture('gif 1.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame)
    # cv.waitKey(0)

    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(2) & 0xFF==ord('d'): # This will prevent from infinite loop
        break

capture.release()
cv.destroyAllWindows()