# In this code we will run the system webcam using opencv and try to take live video for further procssing --------------

#  from turtle import width
import cv2 as cv

def rescaleFrame(frame, scale = 1):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)

# use parameter 0 if using in built webcam
# use parameter 1 for external webcam
cap = cv.VideoCapture(1)

#-----------------------------------------------------------------------------
# Saving the video frames 
# fourcc code is a four byte code to specify the video codec
# DIVX, XVID, MJPG, X264, WMV1, WMV2
#---------------------------------------------------------------------------

fourcc = cv.VideoWriter_fourcc(*"XVID")
# It contain 4 parameters, name, codec, fps, resolution
out = cv.VideoWriter('Output.avi', fourcc, 20.0, (160,120))


print(cap.isOpened())


while cap.isOpened():
    ret, ori = cap.read()
    # rescaled_Frame = rescaleFrame(ori)
    if ret == True:
        print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

        out.write(ori)

        cv.imshow('Frame', ori)

        if cv.waitKey(1) & 0xFF == ord('d'):
            break
    else:
        break
cap.release()
out.release()
cv.destroyAllWindows()