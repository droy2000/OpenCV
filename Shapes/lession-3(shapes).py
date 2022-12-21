# from types import NoneType
import cv2 as cv
import numpy as np

img = cv.imread('images\glass.png')
cv.imshow('glass', img)

# for creating a blank image: -------------------------------------------
#------------------------------------------------------------------------

# create a blank image of low intensity-------------------------------------------------------------

blank = np.zeros((500,500,3), dtype='uint8')# zeros() take height, width, number of colour chanels
cv.imshow('Blank', blank)
cv.imwrite('E:/openCV/Digital-Image-Processing/Shapes/'+ 'blank.png', blank)

# Create an blank image of higher intensity-----------------------------------------------------------

black = np.ones((500,500,3), dtype = None)
cv.imshow('Black', black)
cv.imwrite('E:/openCV/Digital-Image-Processing/Shapes/'+ 'black.png', black)

# paint the image a certain colour------------------------------------------------------------------

img[0:100, 0:500] = 158,0,0  # produce a blue color rectangle in the image
cv.imshow('Blue', img) 
cv.imwrite('E:/openCV/Digital-Image-Processing/Shapes/'+ 'Blue.png', img)

# blank[(width_lower-limit):(height_lower-limt),(width_higher-limit):(height_higher-limit)]
cv.imshow('Blue-', blank)

# create a rectangle in the image window--------------------------------------------------------

cv.rectangle(img, (0,0), (230,230), (0,400,0), thickness=3)
cv.imshow('Rectangle1', img)
cv.imwrite('E:/openCV/Digital-Image-Processing/Shapes/'+ 'Rectangle1.png', img)

# create fill rectangle in the image window-----------------------------------------------------

cv.rectangle(img, (220,220), (280,280), (0,400,0), thickness=-1)
cv.imshow('Rectangle2', img)
cv.imwrite('E:/openCV/Digital-Image-Processing/Shapes/'+ 'Rectangle2.png', img)

# Another way to create the rectangle --------------------------------------------------------

cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,200,0), thickness=cv.FILLED)
cv.imshow('Rectangle3', blank)
cv.imwrite('E:/openCV/Digital-Image-Processing/Shapes/'+ 'Rectangle3.png', img)

# creating a circle -----------------------------------------------------------------------------
cv.circle(img, (img.shape[1]//2, img.shape[0]//2), 50, (0,0,506), thickness=-1)
cv.imshow('Circle', img)
cv.imwrite('E:/openCV/Digital-Image-Processing/Shapes/'+ 'Circle.png', img)

# CREATE A LINE----------------------------------------------------------------------------------
cv.line(blank, (0,0), (215,215), (0,0,200), thickness=3)
cv.imshow('Line', blank)
cv.imwrite('E:/openCV/Digital-Image-Processing/Shapes/'+ 'Line.png', img)

# Get a text on the image window-----------------------------------------------------------------
cv.putText(blank, 'Hello', (225, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,233,0), 2)
cv.imshow('Text', blank)
cv.imwrite('E:/openCV/Digital-Image-Processing/Shapes/'+ 'Text.png', img)
#------------------------------------------------------------------------------------------------

cv.waitKey(0)

print(blank.size)
