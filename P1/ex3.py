#import
import numpy as np
import cv2
import sys

# Read the image
image1 = cv2.imread( sys.argv[1], cv2.IMREAD_UNCHANGED )
image2 = cv2.imread( sys.argv[2], cv2.IMREAD_UNCHANGED )

image_sub12=cv2.subtract(image1, image2)
image_sub21=cv2.subtract(image2, image1)



if  np.shape(image1) == () or np.shape(image2) == ():
	# Failed Reading
	print("Image file could not be open")
	exit(-1)


# Show the image
cv2.imshow( "Image1", image1)
cv2.imshow( "Image2", image2 )

cv2.imshow( "Subtraction12", image_sub12 )
cv2.imshow( "Subtraction21", image_sub21 )

# Wait
cv2.waitKey( 0 )

