
import cv2 as cv
import os

# def rescaleFrame(frame, scale = .2):
#     width  = int(frame.shape[1]*scale)
#     height = int(frame.shape[0]*scale)
#     dimensions = (width, height)

    # return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)


cap = cv.VideoCapture("videos\Pexels_Videos_2103099.mp4")

current_frame = 0

if not os.path.exists('E:/openCV/Digital-Image-Processing/Frame_Capturing/Extracted_frame'):
    os.makedirs('E:/openCV/Digital-Image-Processing/Frame_Capturing/Extracted_frame')

while (True):
    ret, ori = cap.read()

    cv.imshow("Output", ori)
    cv.imwrite('E:/openCV/Digital-Image-Processing/Frame_Capturing/Extracted_frame/'+ str(current_frame) + '.png', ori)
    current_frame  += 1

    if cv.waitKey(1) & 0xFF == ord('d'):
        break


cap.release()
cv.destroyAllWindows()




