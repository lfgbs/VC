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

    #inverting image
    image = cv2.bitwise_not(img_thresholded)

    #circular Structuring 
    circular_struct_point=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11))

    #square structuring point structuring point
    square_struct_point = np.ones((11,11), np.uint8)

    circular_img_dilation = cv2.dilate(image, circular_struct_point, iterations=1)
    square_img_dilation = cv2.dilate(image, square_struct_point, iterations=1)
    square_img_dilation_repeated = cv2.dilate(image, square_struct_point, iterations=5)


    cv2.imshow('original', image)
    cv2.imshow('square dilation', circular_img_dilation)
    cv2.imshow('circular dilation', square_img_dilation)
    cv2.imshow('square dilation iterated', square_img_dilation_repeated)

    cv2.waitKey(0)

if __name__ == "__main__":
    main()