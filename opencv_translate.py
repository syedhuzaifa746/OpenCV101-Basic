# USAGE
# python opencv_translate.py

# import the necessary packages
import numpy as np
import argparse
import imutils
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="opencv_logo.png",
	help="path to the input image")
args = vars(ap.parse_args())

# load the image and display it to our screen
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# shift the image 25 pixels to the right and 50 pixels down
# M = np.float32([[1, 0, 25], [0, 1, 50]])
# shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
# cv2.imshow("Shifted Down and Right", shifted)
# cv2.waitKey(0)

cv2.rectangle(image, (10, 50), (350, 350), (0, 255, 0), 2)

cv2.imshow('Rectangle Example', image)
cv2.waitKey(0)
