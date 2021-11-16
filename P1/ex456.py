#import
import numpy as np
import cv2
import argparse
from functools import partial

def onMouse(event, x, y, flags, params, w_name, img):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 10, color)
        cv2.imshow(w_name, img)

def main():

    parser = argparse.ArgumentParser(description='Typing Test Option Parser')
    parser.add_argument('-i', '--image', type=str, required=True,help='Full path to image file.')
    args = parser.parse_args()

    window_name='window'

    global color
    color=(0,0,255)

    # Read the image
    image = cv2.imread( args.image, cv2.IMREAD_COLOR )
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Convert to gray

    cv2.imshow(window_name, image)
    cv2.imshow('window_name', image_gray)
   

    cv2.setMouseCallback(window_name, partial(onMouse, w_name=window_name, img=image))

    # Wait
    cv2.waitKey( 0 )



if __name__ == '__main__':
    main()