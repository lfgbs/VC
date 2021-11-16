import numpy as np
import cv2
import argparse

def gaussian_blur(img, ksize):
    return cv2.Gaussian_Blur(img,ksize)

def blur_ntimes(img, ksize, ntimes):

    blurred_img=img

    for i in range(ntimes +1):
        blurred_img=gaussian_blur(blurred_img, ksize)

    return blurred_img

def main():

    parser = argparse.ArgumentParser(description='Parser for opening images with opencv.One and only one option must be selected')
    parser.add_argument('--image', type=str, required=True, help='Full path to the image')
    args = parser.parse_args()

    image = cv2.imread(args.image, cv2.IMREAD_GRAYSCALE) # Load an image 

    blur3x3=gaussian_blur(image, 3)
    blur5x5=gaussian_blur(image, 5)
    blur7x7=gaussian_blur(image, 7)
    #blur3x3_3times=blur_ntimes(image, 3, 3)

    cv2.imshow('original', image)
    cv2.imshow('3x3', blur3x3)
    cv2.imshow('5x5', blur5x5)
    cv2.imshow('7x7', blur7x7)
    #cv2.imshow('7x7 3 times', blur3x3_3times)

    cv2.waitKey(0)


if __name__ == '__main__':
    main()