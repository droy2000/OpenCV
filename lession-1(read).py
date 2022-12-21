import cv2 as cv
# Reading Image ------------------------------

img = cv.imread('python\cvpython\glass.png')

# new_image = cv.cvtColor(img, cv.COLOR_GRAY2BGR)

cv.imshow('glass', img) #This will open a new window named as glass with the image file in img
# cv.imshow('new', new_image)
cv.waitKey(0)


# Reading videos ----------------------------------
#--------------------------------------------------

capture = cv.VideoCapture('gif 1.mp4')

"""Video Capture take interger or file as an argument. 
Integer is given as an argument when webcam or any camerais used. 
If any video file is present then argumet is path of the file"""

while True:
    isTrue, frame = capture.read()     #frame will capture the video frame by frame 

    cv.imshow('Video', frame)

    if cv.waitKey(2) & 0xFF==ord('d'): # This will prevent from infinite loop
        break
capture.release()
cv.destroyAllWindows()




