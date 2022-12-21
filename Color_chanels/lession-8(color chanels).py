import cv2 as cv
import numpy as np
# import matplotlib.pyplot as plt

original = cv.imread('images\DSC00823.jpg')

# Rescale image --------------------------------------------------------------
def rescaleFrame(frame, scale = 0.3):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)

img = rescaleFrame(original)
cv.imshow('Image', img)

# we can split the color chanels of the image -----------------------------------------
b,g,r = cv.split(img)

cv.imshow('Blue', b)
cv.imwrite('E:/openCV/Digital-Image-Processing/Color chanels/' + 'Blue chanel.png', b)
cv.imshow('Green', g)
cv.imwrite('E:/openCV/Digital-Image-Processing/Color chanels/' + 'Green chanel.png', g)
cv.imshow('Red', r)
cv.imwrite('E:/openCV/Digital-Image-Processing/Color chanels/' + 'Red chanel.png', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# Merge the 3 chanels -----------------------------------------------------
merged = cv.merge([b,g,r])
cv.imshow('Merged',merged)
cv.imwrite('E:/openCV/Digital-Image-Processing/Color chanels/' + 'Merged chanels.png', merged)


# Setting specific color chanel as a blank image --------------------------- 

blank = np.zeros(img.shape[:2], dtype='uint8')

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue1', blue)
cv.imshow('Green1', green)
cv.imshow('Red1', red)

cv.imwrite('E:/openCV/Digital-Image-Processing/Color chanels/' + 'Blue specific.png', blue)
cv.imwrite('E:/openCV/Digital-Image-Processing/Color chanels/' + 'Green specific.png', green)
cv.imwrite('E:/openCV/Digital-Image-Processing/Color chanels/' + 'Red specific.png', red)

# merged1 = cv.merge([blue,green,red, blank])
# cv.imshow('Merged1', merged1)
cv.waitKey(0)