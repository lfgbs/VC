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

    #circular Structuring point
    circular_struct_point=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11))

    #square structuring point 
    square_struct_point = np.ones((11,11), np.uint8)

    #11x1 structuring point
    struct_point_11x1=cv2.getStructuringElement(cv2.MORPH_RECT,(11, 1))

    #skewed anchor
    skewed_anchor_struct=cv2.getStructuringElement(cv2.MORPH_RECT,(11,11), anchor=(1,2))


    circular_img_erosion = cv2.erode(image, circular_struct_point, iterations=1)
    square_img_erosion = cv2.erode(image, square_struct_point, iterations=1)
    square_img_erosion_repeated = cv2.erode(image, square_struct_point, iterations=5)
    circular_img_erosion_repeated = cv2.erode(image, circular_struct_point, iterations=5)
    img_erosion_11x1 = cv2.erode(image, struct_point_11x1, iterations=1)
    img_erosion_skewed = cv2.erode(image, skewed_anchor_struct, iterations=1)



    cv2.imshow('original', image)
    cv2.imshow('square erosion', circular_img_erosion)
    cv2.imshow('circular erosion', square_img_erosion)
    cv2.imshow('square erosion iterated', square_img_erosion_repeated)
    cv2.imshow('circular erosion iterated', circular_img_erosion_repeated)
    cv2.imshow('11x1 erosion', img_erosion_11x1)
    cv2.imshow('skewed anchor', img_erosion_skewed)

    cv2.waitKey(0)

if __name__ == "__main__":
    main()