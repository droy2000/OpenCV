import cv2 as cv
import numpy as np

img = cv.imread('E:\openCV\images\DSC00823.jpg')
# img = cv.resize(capture, (400,250), interpolation= cv.INTER_AREA)
cv.imshow('Original', img)

# CONVERTING BGR IMAGE TO GRAY SCALE IMAGE-------------------------------------------------------------------------

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
cv.imwrite('E:/openCV/Digital-Image-Processing/Essential_Functions/'+ 'Gray.png', gray)

color = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
cv.imshow('Color', color)
# cv.imwrite('E:/openCV/Digital-Image-Processing/Essential_Functions/'+ 'Color.png', color)

# BLURING THE IMAGE ------------------------------------------------------------------------------------------------

blur = cv.GaussianBlur(img, (5,7), cv.BORDER_DEFAULT) # (x,y) is the GaussianBlur function is the blur level
cv.imshow('Blur', blur)
cv.imwrite('E:/openCV/Digital-Image-Processing/Essential_Functions/'+ 'Blur.png', blur)

# EDGE CASCADE -------------------------------------------------------------------------------------------------------

canny = cv.Canny(img, 100,100)
cv.imshow('Canny', canny)
cv.imwrite('E:/openCV/Digital-Image-Processing/Essential_Functions/'+ 'Canny_Edges.png', canny)

# we can reduce the edges by applying blur to the image before edge cascade------------------------------------------=

srt = cv.Canny(blur, 100,100)
cv.imshow('SRT', srt)


# DIALATING THE IMAGE (image is dialated using edges of the image)-----------------------------------------------------

dilate = cv.dilate(canny, (3,3), iterations=5)
cv.imshow('Dilatd', dilate)
cv.imwrite('E:/openCV/Digital-Image-Processing/Essential_Functions/'+ 'Dilated.png', dilate)

# ERODING (we can get back the edges of the image back by eroging the dialatd image)---------------------------------------

eroded = cv.erode(dilate, (3,3), iterations=5)
cv.imshow('Eroded', eroded)
cv.imwrite('E:/openCV/Digital-Image-Processing/Essential_Functions/'+ 'Eroded.png', eroded)

# CROPPED -------------------------------------------------------------------------------------------------------------------

cropped = img[500:700, 200:400]
cv.imshow('Cropped', cropped)
cv.imwrite('E:/openCV/Digital-Image-Processing/Essential_Functions/'+ 'Cropped.png', cropped)

cv.waitKey(0)