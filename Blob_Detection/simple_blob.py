import cv2 as cv
import numpy as np

# Load Input image file
img = cv.imread("E:\\openCV\Extracted_frame\\1.png",0)


# Set up the detector with default parameters
detector = cv.SimpleBlobDetector_create()
cv.imshow("Original image", img)

# Detect blobs
keypoint_info = detector.detect(img)

# Highlight detected blobs as blue circles. 
blank = np.zeros((500,500, 3), dtype = None)
blobs = cv.drawKeypoints(img, keypoint_info, np.array([]), (255, 0, 0), cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Display Blobs in the image
cv.imshow("Blobs", blobs)
cv.waitKey(0)
cv.destroyAllWindows()