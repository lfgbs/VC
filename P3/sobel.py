import numpy as np
import cv2
import argparse

def main():

    parser = argparse.ArgumentParser(description='Parser for opening images with opencv.One and only one option must be selected')
    parser.add_argument('--image', type=str, required=True, help='Full path to the image')
    args = parser.parse_args()

    ddepth = cv2.CV_64F

    image = cv2.imread(args.image, cv2.IMREAD_GRAYSCALE) # Load an image 

    sobelx=cv2.Sobel(image, ddepth, 1, 0, 5)
    sobely=cv2.Sobel(image, ddepth, 0, 1, 5)
    sobelxy=cv2.Sobel(image, ddepth, 1, 1, 5)


    cv2.imshow('original', image)
    cv2.imshow('sobelx', sobelx)
    cv2.imshow('sobely', sobely)
    cv2.imshow('sobelxy', sobelxy)

    cv2.waitKey(0)


if __name__ == '__main__':
    main()