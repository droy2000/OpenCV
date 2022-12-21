from turtle import width
import cv2 as cv
import numpy as np
import matplotlib as plt

# from macpath import dirname

def rescaleFrame(frame, scale = .2):
    width = int(frame.shape[1]* scale)
    height = int(frame.shape[0]* scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)

cap = cv.VideoCapture('videos\pexels-kelly-lacy-6595761.mp4')
_,cap_img = cap.read()

# Rescaling the frame ratio--------------------------------------------------------------

f_image = rescaleFrame(cap_img)
# cv.imshow('1st Image', f_image)

# Converting the image to gray-scale image ---------------------------------------------
gray_img = cv.cvtColor(f_image, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray image', gray_img)

# Thrasholding the image ---------------------------------------------------------------------
ret, thrash = cv.threshold(gray_img, 50,255, cv.THRESH_BINARY)
# cv.imshow('Threshold image', thrash)

# Blurring the background for better object clearance ---------------------------------------
blurr = cv.GaussianBlur(thrash, (13,13), cv.BORDER_DEFAULT)
# cv.imshow('Blurred image', blurr)

canny = cv.Canny(blurr, 100, 125)
cv.imshow('Canny image', canny)


while True:
    isTrue, frame = cap.read()
    video0 = rescaleFrame(frame)
    # cv.imshow('color', video0)
    # blurr_video = cv.GaussianBlur(video0, (5,7), cv.BORDER_DEFAULT)
    video = cv.cvtColor(video0, cv.COLOR_BGR2GRAY)
    # cv.imshow('Gray Video', video)
    canny_video = cv.Canny(video, 100, 125)
    # cv.imshow('Video', canny_video)
    ret, thrash_video = cv.threshold(video, 50,255, cv.THRESH_BINARY)
    cv.imshow('Thrash Video', thrash_video)

    # diff = cv.bitwise_or(canny, thrash_video)
    # cv.imshow('Clipping', diff)
    
    diff1 = cv.absdiff(gray_img, video)
    cv.imshow('Clipping1', diff1)
    # ret, last_thrash = cv.threshold(diff1, 75, 255, cv.THRESH_BINARY)
    # cv.imshow('Result', last_thrash)

    # diff2 = cv.bitwise_xor(canny, thrash_video)
    # cv.imshow('Clipping2', diff2)

    if cv.waitKey(15) & 0xFF==ord('d'):
        break
cap.release()
cv.destroyAllWindow()

cv.waitKey(0)


