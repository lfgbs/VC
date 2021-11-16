#!/usr/bin/python3
import cv2
import argparse
import numpy as np


def threshold_img(img, thresh_type):
    if thresh_type==cv2.THRESH_BINARY:
        retval, img_thresholded = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    if thresh_type==cv2.THRESH_BINARY_INV:
        retval, img_thresholded = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

    if thresh_type==cv2.THRESH_TRUNC:
        retval, img_thresholded = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)

    if thresh_type==cv2.THRESH_TOZERO:
        retval, img_thresholded = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
        
    if thresh_type==cv2.THRESH_TOZERO_INV:
        retval, img_thresholded = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

    return img_thresholded

def main():

    parser = argparse.ArgumentParser(description='Parser for opening images with opencv.One and only one option must be selected')
    parser.add_argument('--image', type=str, required=True, help='Full path to the image')
    args = parser.parse_args()

    image = cv2.imread(args.image, cv2.IMREAD_UNCHANGED) # Load an image 

    if  np.shape(image) == ():
        # Failed Reading
        print("Image file could not be open!")
        exit(-1)

    # Image characteristics
    if len (image.shape) > 2:
        print ("The loaded image is NOT a GRAY-LEVEL image !")
        exit(-1)

    binary_thresholded=threshold_img(image, cv2.THRESH_BINARY)
    binary_inverted_thresholded=threshold_img(image, cv2.THRESH_BINARY_INV)
    trunc_thresholded=threshold_img(image, cv2.THRESH_TRUNC)
    tozero_thresholded=threshold_img(image, cv2.THRESH_TOZERO)
    tozero_inverted_thresholded=threshold_img(image, cv2.THRESH_TOZERO_INV)



    cv2.imshow('binary', binary_thresholded)  # Display the image
    cv2.imshow('binary inverted', binary_inverted_thresholded)
    cv2.imshow('trunc', trunc_thresholded)
    cv2.imshow('tozero', tozero_thresholded)
    cv2.imshow('tozero inverted', tozero_inverted_thresholded)
    cv2.imshow('original', image)  # Display the image
    cv2.waitKey(0) # wait for a key press before proceeding

if __name__ == '__main__':
    main()