import cv2 as cv
import numpy as np

img = cv.imread('images\glass.png')
cv.imshow('Original', img)

# Translation ------------------------------------------------------------

def translation(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


# -x --> Left
# -y --> Up
# x --> Right 
# y --> Down

translated = translation(img, 100, 100)
cv.imshow('Translate', translated)
cv.imwrite('E:/openCV/Digital-Image-Processing/Basic operation on Image/' + 'Tranlate.png', translated)


# Rotation ---------------------------------------------------------------

def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45)
cv.imshow('Rotated', rotated)
cv.imwrite('E:/openCV/Digital-Image-Processing/Basic operation on Image/' + 'Rotated1.png', rotated)

r_rotated = rotate(rotated, 45)
cv.imshow('r_Rotated', r_rotated)
cv.imwrite('E:/openCV/Digital-Image-Processing/Basic operation on Image/' + 'Rotated2.png', r_rotated)


# Resizing
resized = cv.resize(img,(500,500), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resized)
cv.imwrite('E:/openCV/Digital-Image-Processing/Basic operation on Image/' + 'Resized.png', resized)

# Filliping 
flip = cv.flip(img,-1)
cv.imshow('Flipped', flip)
cv.imwrite('E:/openCV/Digital-Image-Processing/Basic operation on Image/' + 'Flipped.png', flip)


# Cropping ---------------------------------------------------------------
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)
cv.waitKey(0)
cv.imwrite('E:/openCV/Digital-Image-Processing/Basic operation on Image/' + 'Cropping.png', cropped)




