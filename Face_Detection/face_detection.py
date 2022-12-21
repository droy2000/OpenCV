import cv2 as cv
import os

# Different cascades are used for face detection-----------------------
# Haar Cascade is used in this piece of code -------------------------------------
faceCascade = cv.CascadeClassifier("Digital-Image-Processing\haarcascade_frontalface_default.xml")

# Source image----------------------
img = cv.imread("images\potrait.jpg")
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Detect the face the the input image--------------------------------------
faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

# Draw the rectangular box around the detected face-----------------------------------
for (x,y,w,h) in faces:
    cv.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

# Result-----------------------------------------------------------------------
cv.imshow('Image', img)

# Saving the Result---------------------------------------------------------
cv.imwrite('E:/openCV/Digital-Image-Processing/Face Detection/'+ 'detected face.png', img)


cv.waitKey(0)



