import cv2 as cv
import numpy as np

img = cv.imread('images\Face.png')
cv.imshow('Original', img)

blank = np.zeros(img.shape[:2], dtype = 'uint8',)
# cv.imshow('Blank', blank)
cv.imwrite('E:/openCV/Digital-Image-Processing/Image Masking/' + 'Blank.png', blank)

# Creating the mask ------------------------------------------------------
mask1 = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2),300,  255, -1)
cv.imshow('Mask1', mask1)
cv.imwrite('E:/openCV/Digital-Image-Processing/Image Masking/' + 'Mask1.png', mask1)

mask2 = cv.rectangle(blank.copy(), (100,0),(600,600), 255, -1)
cv.imshow('Mask2', mask2)
cv.imwrite('E:/openCV/Digital-Image-Processing/Image Masking/' + 'Mask2.png', mask2)

# Masked image ------------------------------------------------------------------
masked1 = cv.bitwise_and(img,img, mask = mask1)
cv.imshow('Masked Image1', masked1)
cv.imwrite('E:/openCV/Digital-Image-Processing/Image Masking/' + 'Masked1.png', masked1)

masked2 = cv.bitwise_and(img, img, mask = mask2)
cv.imshow('Masked Image 2', masked2)
cv.imwrite('E:/openCV/Digital-Image-Processing/Image Masking/' + 'Masked2.png', masked2)



cv.waitKey(0)