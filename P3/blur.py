import numpy as np
import cv2
import argparse

def printImageFeatures(image):
	# Image characteristics
	if len(image.shape) == 2:
		height, width = image.shape
		nchannels = 1
	else:
		height, width, nchannels = image.shape

	# print some features
	print("Image Height: %d" % height)
	print("Image Width: %d" % width)
	print("Image channels: %d" % nchannels)
	print("Number of elements : %d" % image.size)

def blur(img, ksize):
    return cv2.blur(img, (ksize, ksize))

def blur_ntimes(img, ksize, ntimes):

    blurred_img=img

    for i in range(ntimes +1):
        blurred_img=blur(blurred_img, ksize)

    return blurred_img

def main():

    parser = argparse.ArgumentParser(description='Parser for opening images with opencv.One and only one option must be selected')
    parser.add_argument('--image', type=str, required=True, help='Full path to the image')
    args = parser.parse_args()

    image = cv2.imread(args.image, cv2.IMREAD_GRAYSCALE) # Load an image 

    blur3x3=blur(image, 3)
    blur5x5=blur(image, 5)
    blur7x7=blur(image, 7)
    blur7x7_3times=blur_ntimes(image, 7, 3)

    cv2.imshow('original', image)
    cv2.imshow('3x3', blur3x3)
    cv2.imshow('5x5', blur5x5)
    cv2.imshow('7x7', blur7x7)
    cv2.imshow('7x7 3 times', blur7x7_3times)

    cv2.waitKey(0)


if __name__ == '__main__':
    main()