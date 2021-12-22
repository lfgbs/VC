import argparse
import cv2
import numpy as np

def main():
    parser = argparse.ArgumentParser(description='Parser for opening images with opencv.One and only one option must be selected')
    parser.add_argument('--image', type=str, required=True, help='Full path to the image')
    args = parser.parse_args()

    image = cv2.imread(args.image, cv2.IMREAD_GRAYSCALE) # Load an image 

    #converting to binary with threshold of 120
    retval, img_thresholded = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY)

    #circular Structuring 
    circular_struct_point=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11))

    struct_point_9x3=cv2.getStructuringElement(cv2.MORPH_RECT,(9,3))
    struct_point_3x9=cv2.getStructuringElement(cv2.MORPH_RECT,(3,9))

    #circular opening
    open_image_circle=cv2.morphologyEx(image, cv2.MORPH_OPEN, circular_struct_point)

    #9x3 opening
    open_image_9x3 = cv2.morphologyEx(image, cv2.MORPH_OPEN, struct_point_9x3)

    #9x3 opening
    open_image_3x9 = cv2.morphologyEx(image, cv2.MORPH_OPEN, struct_point_3x9)


    cv2.imshow('original', image)
    cv2.imshow('opening circle', open_image_circle)
    cv2.imshow('opening 9x3', open_image_9x3)
    cv2.imshow('opening 3x9', open_image_3x9)


    cv2.waitKey(0)

if __name__ == "__main__":
    main()