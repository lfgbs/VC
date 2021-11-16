import numpy as np
import cv2
import argparse

def main():

    parser = argparse.ArgumentParser(description='Parser for opening images with opencv.One and only one option must be selected')
    parser.add_argument('--image', type=str, required=True, help='Full path to the image')
    args = parser.parse_args()

    image = cv2.imread(args.image, cv2.IMREAD_GRAYSCALE) # Load an image 

    #canny=cv2.Canny(image, 100, 75)
    #canny=cv2.Canny(image, 1, 255)
    canny=cv2.Canny(image, 220, 255)

    cv2.imshow('original', image)
    cv2.imshow('canny', canny)

    cv2.waitKey(0)


if __name__ == '__main__':
    main()