import cv2 as cv
import numpy as np

img = cv.imread('images\glass.png')
cv.imshow('Original', img)


# Blank Image ---------------------------------------------------------------------------------------------------
blank = np.zeros(img.shape, dtype = 'uint8')
cv.imshow('Blank', blank)

# Edges of the original image -------------------------------------------------------------------------------------
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny edges', canny)
cv.imwrite('E:/openCV/Digital-Image-Processing/Image Contours/'+ 'Canny.png', canny)

# Gray scale image -------------------------------------------------------------------------------------------------
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
cv.imwrite('E:/openCV/Digital-Image-Processing/Image Contours/'+ 'Gray.png', gray)

# Thresholding of Image --------------------------------------------------------------------------------------------
ret, thresh = cv.threshold(gray, 125,255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)
cv.imwrite('E:/openCV/Digital-Image-Processing/Image Contours/'+ 'Thrashold.png', thresh)

# Finding contours---------------------------------------------------------------------------------------------------
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

# Draw contours on blank image ------------------------------------------------------------------------------------------------------
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours_Drawn', blank)
cv.imwrite('E:/openCV/Digital-Image-Processing/Image Contours/'+ 'Contours.png', blank)
#----------------------------------------------------------------------------------------------------------------------
cv.waitKey(0)
