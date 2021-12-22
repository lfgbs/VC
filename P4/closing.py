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
    circular_struct_point=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(23,23))
    big_circular_struct_point=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(40,40))
    small_circular_struct_point=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(10,10))

    #circular closing
    closed_image_circle=cv2.morphologyEx(image, cv2.MORPH_CLOSE, circular_struct_point)
    big_closed_image_circle=cv2.morphologyEx(image, cv2.MORPH_CLOSE, big_circular_struct_point)
    small_closed_image_circle=cv2.morphologyEx(image, cv2.MORPH_CLOSE, small_circular_struct_point)


    cv2.imshow('original', image)
    cv2.imshow('closing circle', closed_image_circle)
    cv2.imshow('big_closed_image_circle', big_closed_image_circle)
    cv2.imshow('small_closed_image_circle', small_closed_image_circle)


    cv2.waitKey(0)

if __name__ == "__main__":
    main()