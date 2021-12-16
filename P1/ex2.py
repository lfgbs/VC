#import
import numpy as np
import cv2
import sys

# Read the image
image = cv2.imread( sys.argv[1], cv2.IMREAD_GRAYSCALE )

img_copy=image.copy()


if  np.shape(image) == ():
	# Failed Reading
	print("Image file could not be open")
	exit(-1)

# Image characteristics
height, width= image.shape

for i in range(height):
    for j in range(width):
        if img_copy[i,j]<128:
            img_copy[i,j]=0

# Show the image
cv2.imshow( "Original", image )
cv2.imshow( "Tampered", img_copy )


# Wait
cv2.waitKey( 0 )
