# USAGE
# python basic_drawing.py

# import the necessary packages
import numpy as np
import cv2

# initialize our canvas as a 300x300 pixel image with 3 channels
# (Red, Green, and Blue) with a black background
canvas = np.zeros((300, 300, 3), dtype="uint8")

# draw a green line from the top-left corner of our canvas to the
# bottom-right
green = (0,255,0)
cv2.line(canvas, (0, 0),(300, 300), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# draw a 3 pixel thick red line from the top-right corner to the
# bottom-left
red  = (0,0,255)
cv2.line(canvas, (300,0),(0,300),red, 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# draw a green 50x50 pixel square, starting at 10x10 and ending at 60x60
cv2.rectangle(canvas, (10,10), (60,60), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# re-initialize our canvas as an empty array, then compute the
# center (x, y)-coordinates of the canvas
canvas = np.zeros((300, 300, 3), dtype="uint8")
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
white = (255, 255, 255)

# loop over increasing radii, from 25 pixels to 150 pixels in 25
# pixel increments
for r in range(0, 175, 25):
	# draw a white circle with the current radius size
	cv2.circle(canvas, (centerX, centerY), r, white)

# show our work of art
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)