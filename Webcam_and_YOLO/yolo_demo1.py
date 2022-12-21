import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

whT = 320
 
classesFile = 'Digital-Image-Processing\coco.names'
classNames = []
with open(classesFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')
print(classNames)  
print(len(classNames))


modelConfiguration = 'Digital-Image-Processing\Webcam\yolov3-320.cfg'
modelWeights = 'Digital-Image-Processing\Webcam\yolov3.weights'

net = cv.dnn.readNetFromDarknet(modelConfiguration, modelWeights)
net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv.dnn.DNN_TARGET_CPU)


while True:
    ret, img = cap.read()

    blob = cv.dnn.blobFromImage(img, 1/255, (whT, whT), [0,0,0], 1, crop = False)
    net.setInput(blob)

    layerNames = net.getLayerNames()
    print(layerNames)
    
    

    

 

    cv.imshow('Image', img)
    cv.waitKey(1)