import argparse
import cv2
import numpy as np

def main():
    parser = argparse.ArgumentParser(description='Parser for opening images with opencv.One and only one option must be selected')
    parser.add_argument('--image', type=str, required=True, help='Full path to the image')
    args = parser.parse_args()

    image = cv2.imread(args.image, cv2.IMREAD_GRAYSCALE) # Load an image 

    #converting to binary with threshold of 120
    retval, img_thresholded = cv2.threshold(image, 90, 255, cv2.THRESH_BINARY)

    #inverting image
    image = cv2.bitwise_not(img_thresholded)

    #circular Structuring point
    circular_struct_point=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11))

    #square struct point
    square_struct_point=cv2.getStructuringElement(cv2.MORPH_RECT,(9,9))

    circular_img_erosion = cv2.erode(image, circular_struct_point, iterations=2)
    square_img_erosion = cv2.erode(image, square_struct_point, iterations=2)


    cv2.imshow('original', image)
    cv2.imshow('circular erosion', circular_img_erosion)
    cv2.imshow('square erosion', square_img_erosion)


    cv2.waitKey(0)

if __name__ == "__main__":
    main()