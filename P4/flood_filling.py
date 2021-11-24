import argparse
import cv2
import numpy as np
from functools import partial

def onMouse(event, x, y, flags, param, w_name, img, mask):
     if event==cv2.EVENT_LBUTTONDOWN:
        seed=(x,y)
        num,flooded,mask,rect = cv2.floodFill(img, mask ,seed, 255, 5, 5)
        cv2.imshow(w_name, flooded)

def main():
    parser = argparse.ArgumentParser(description='Parser for opening images with opencv.One and only one option must be selected')
    parser.add_argument('--image', type=str, required=True, help='Full path to the image')
    args = parser.parse_args()

    window_name="flood fill"

    image = cv2.imread(args.image, cv2.IMREAD_GRAYSCALE) # Load an image
    cv2.imshow(window_name, image)

    h,w= image.shape

    mask = np.zeros((h+2,w+2),np.uint8)

    #converting to binary with threshold of 120
    #retval, img_thresholded = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY)
    cv2.setMouseCallback(window_name, partial(onMouse, w_name=window_name, img=image, mask=mask))

    cv2.waitKey(0)

if __name__ == "__main__":
    main()