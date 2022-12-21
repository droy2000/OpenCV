from statistics import median_grouped
import cv2 as cv

original = cv.imread('images\DSC00823.jpg')

def rescaleFrame(frame, scale = 0.3):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)


img = rescaleFrame(original)
cv.imshow('Image', img)

# Averaging ---------------------------------------------------
average = cv.blur(img, (7,7)) # heigher the value (x,x), higher the blur 
cv.imshow('Average Blur', average)
cv.imwrite('E:/openCV/Digital-Image-Processing/Smoothing Bluring/' + 'Averaging.png', average)

# Gaussian Blur ---------------------------------------------------------
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian Blur', gauss)
cv.imwrite('E:/openCV/Digital-Image-Processing/Smoothing Bluring/' + 'Gaussian Blur.png', gauss)

# Median Blur -------------------------------------------------
median = cv.medianBlur(img, 7)
cv.imshow('Median Blur', median)
cv.imwrite('E:/openCV/Digital-Image-Processing/Smoothing Bluring/' + 'Median.png', median)

# Bilateral Blur -------------------------------------------------------------
bilateral = cv.bilateralFilter(img, 5, 45, 35)
cv.imshow('Bilateral', bilateral)
cv.imwrite('E:/openCV/Digital-Image-Processing/Smoothing Bluring/' + 'Bilateral.png', bilateral)

cv.waitKey(0)
