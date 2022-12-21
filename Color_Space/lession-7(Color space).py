import cv2 as cv
# import numpy as np
import matplotlib.pyplot as plt


original = cv.imread('images\DSC00823.jpg')
# cv.imshow('Original', original)

# Rescaled image ----------------------------------------------------------
def rescaleFrame(frame, scale=0.3):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)

img = rescaleFrame(original)
cv.imshow('Image', img)
cv.imwrite('E:/openCV/Digital-Image-Processing/Color Space/'+ 'Rescaled_Frame.png', img)

# when we provide BGR image to matplot it will convert it in RGB----------------
# Therefore there is inversion in the color of the image--------------------------

plt.imshow(img)
plt.show()

# BGR to Grayscale ----------------------------------------------------------

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
cv.imwrite('E:/openCV/Digital-Image-Processing/Color Space/'+ 'Gray.png', gray)

# BGR to HSV -----------------------------------------------------------------
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)
cv.imwrite('E:/openCV/Digital-Image-Processing/Color Space/'+ 'HSV.png', hsv)

# BGR to LAB -------------------------------------------------------------------
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('Lab', lab)
cv.imwrite('E:/openCV/Digital-Image-Processing/Color Space/'+ 'LAB.png', lab)

# BGR to RGB -------------------------------------------------------------------------
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('Rgb', rgb)
cv.imwrite('E:/openCV/Digital-Image-Processing/Color Space/'+ 'RGB.png', rgb)

#now as we provide image to matplot it will inverse the format of the image--------------------------
plt.imshow(rgb)
plt.show()

# HSV to BGR -----------------------------------------------------------------------
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV_BGR', hsv_bgr)
cv.imwrite('E:/openCV/Digital-Image-Processing/Color Space/'+ 'HSV_BGR.png', hsv_bgr)

# lAB to BGR -----------------------------------------------------------------------
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('Lab_Bgr', lab_bgr)
cv.imwrite('E:/openCV/Digital-Image-Processing/Color Space/'+ 'LAB_BGR.png', lab_bgr)

cv.waitKey(0)
    

