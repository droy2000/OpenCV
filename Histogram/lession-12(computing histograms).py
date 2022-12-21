import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('images\glass.png')
cv.imshow('Image', img)

# Creating histogram of the image --------------------------------------------------------------------
gray_hist = cv.calcHist([img], [0], None, [256], [0,256])

plt.figure() 

plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('no. of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()
plt.savefig('Grayscale Histogram.png')

blank = np.zeros(img.shape[:2], dtype = 'uint8')
circle_mask2 = cv.circle(blank, (img.shape[1]//2, img.shape[0]//3), 300, 233, -1)

# # masked image -------------------------------------------------------------------------------------------------------------
circle_mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//3), 200, 233, -1)
cv.imshow('Mask', circle_mask)

masked_image1 = cv.bitwise_and(img, img, mask=circle_mask)
cv.imshow('Masked_image', masked_image1)

# Histogram of the masked grayscale image ------------------------------------------------------------------------------------------------------
gray_hist1 = cv.calcHist([img], [0], circle_mask, [256], [0,256])

plt.figure()

plt.title('Histogram of Masked Image')
plt.xlabel('Bins')
plt.ylabel('no. of pixels')
plt.plot(gray_hist1)
plt.xlim([0,256])
plt.show()
plt.savefig('E:/openCV/Digital-Image-Processing/Histogram/' + 'Histogram of Masked Image.png')

# COLORED HISTOGRAM----------------------------------------------------------------------------------------------------------------------------------
color_img = cv.imread('python\cvpython\Face.png')
cv.imshow('Color Image', color_img)

# histogram for colored image---------------------------------------------------------------------------------------------------------------
plt.figure()
plt.title('Colored Histogram')
plt.xlabel('Bins')
plt.ylabel('No. of pixels')
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    hist = cv.calcHist([color_img], [i], None, [256], [0,256])
    plt.plot(hist, color= col)
    plt.xlim([0,256])
plt.show()

# Creating mask for colored image ---------------------------------------------------------------------------------------------------------------------
blank = np.zeros(color_img.shape[:2], dtype = 'uint8')

circle_mask2 = cv.circle(blank, (color_img.shape[1]//2, color_img.shape[0]//2), 300, 233, -1)
Face_masked = cv.bitwise_and(color_img, color_img, mask= circle_mask2)
cv.imshow('Masked face', Face_masked)

# histogram for masked colored image ---------------------------------------------------------------------------------------------------------
plt.figure()
plt.title('Masked Color Histogram')
plt.xlabel('Bins')
plt.ylabel('No. of Pixels')
color = ('b', 'g', 'r')
for j, col in enumerate(color):
    hist2 = cv.calcHist([color_img], [j], circle_mask2, [256], [0,256])
    plt.plot(hist2, color= col)
    plt.xlim([0,256])
plt.show()


cv.waitKey(0)
