import numpy as np
import cv2
from matplotlib import pyplot as plt
import argparse

def main():

    parser = argparse.ArgumentParser(description='Parser for opening images with opencv.One and only one option must be selected')
    parser.add_argument('--image', type=str, required=True, help='Full path to the image')
    args = parser.parse_args()

    image = cv2.imread( args.image , cv2.IMREAD_UNCHANGED )

    if  np.shape(image) == ():
        # Failed Reading
        print("Image file could not be open!")
        exit(-1)

    # Image characteristics
    if len (image.shape) > 2:
        #print ("The loaded image is NOT a GRAY-LEVEL image !")
        #exit(-1)
        image = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)

    cv2.imshow("Original Image", image)

    # print some features
    height, width = image.shape
    nchannels = 1
    print("Image Size: (%d,%d)" % (height, width))
    print("Image Type: %d" % nchannels)
    print("Number of elements : %d" % image.size)

    print("Image Size: (%d,%d)" % (height, width))

    min_value, max_value, min_index, max_index = cv2.minMaxLoc(image)
 
    stretched_img=image.copy()

    for i in range(height):
        for j in range(width):
            stretched_img[i,j]=(image[i,j]-min_value)*255/(max_value-min_value)

    # Size
    histSize = 256	 # from 0 to 255
    # Intensity Range
    histRange = [0, 256]

    # Compute the histogram
    hist_item = cv2.calcHist([stretched_img], [0], None, [histSize], histRange)

    ##########################################
    # Drawing with openCV
    # Create an image to display the histogram
    histImageWidth = 512
    histImageHeight = 512
    color = (125)
    histImage = np.zeros((histImageWidth,histImageHeight,1), np.uint8)

    # Width of each histogram bar
    binWidth = int (np.ceil(histImageWidth*1.0 / histSize))

    # Normalize values to [0, histImageHeight]
    cv2.normalize(hist_item, hist_item, 0, histImageHeight, cv2.NORM_MINMAX)

    # Draw the bars of the nomrmalized histogram
    for i in range (histSize):
        cv2.rectangle(histImage,  ( i * binWidth, 0 ), ( ( i + 1 ) * binWidth, int(hist_item[i]) ), (125), -1)

    # ATTENTION : Y coordinate upside down
    histImage = np.flipud(histImage)

    cv2.imshow("stretched Image", stretched_img)
    cv2.imshow('colorhist', histImage)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()