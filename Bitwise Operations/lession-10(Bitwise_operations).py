import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype= 'uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imwrite('E:/openCV/Digital-Image-Processing/Bitwise Operations/'+ 'Rectangle.png', rectangle)

cv.imshow('Circle', circle)
cv.imwrite('E:/openCV/Digital-Image-Processing/Bitwise Operations/'+ 'Circle.png', circle)

# bitwise NOT -------------------------------------------------------------------
bitwise_not1 = cv.bitwise_not(rectangle)
cv.imshow('Not-rectangle', bitwise_not1)
cv.imwrite('E:/openCV/Digital-Image-Processing/Bitwise Operations/'+ 'Not Rectangle.png', bitwise_not1)

bitwise_not2 = cv.bitwise_not(circle)
cv.imshow('NOT-circle', bitwise_not2)
cv.imwrite('E:/openCV/Digital-Image-Processing/Bitwise Operations/'+ 'Not Circle.png', bitwise_not2)

# bitwise AND (find the intersection regions) ------------------------------------------------------------------
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('And', bitwise_and)
cv.imwrite('E:/openCV/Digital-Image-Processing/Bitwise Operations/'+ 'And.png', bitwise_and)

# bitwise OR (find the intersecting and non-intersecting regions) ---------------------------------------------------------------
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Or', bitwise_or)
cv.imwrite('E:/openCV/Digital-Image-Processing/Bitwise Operations/'+ 'Or.png', bitwise_or)

# bitwise XOR (find the non-intersecting regions) ----------------------------------------------------------------
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Xor', bitwise_xor)
cv.imwrite('E:/openCV/Digital-Image-Processing/Bitwise Operations/'+ 'Xor.png', bitwise_xor)

cv.waitKey(0)
