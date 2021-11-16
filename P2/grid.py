# Aula_02_ex_01.py
#
# Drawing of 2D primitives and user Interaction
#
# Paulo Dias - 09/2021


# import
import numpy as np
import cv2
import argparse
from functools import partial

def grid(img, cell_size,w_name):
    color=(0,0,0)
    dimensions = img.shape

    if len(dimensions)<3:
        color=(255,255,255)

    for i in range(0, dimensions[0], cell_size):
        cv2.line(img, (i,0), (i, dimensions[1]), color)

    for j in range(0, dimensions[1], cell_size): 
        cv2.line(img, (0,j), (dimensions[0], j), color)
        print(j)

    cv2.imshow(w_name, img)


def main():

    parser = argparse.ArgumentParser(description='Parser for opening images with opencv.One and only one option must be selected')
    parser.add_argument('--image', type=str, required=True, help='Full path to the image')
    args = parser.parse_args()

    gray_window_name='grided_image_gray'
    color_window_name='grided image color'
    cell_size=20

    image = cv2.imread(args.image, cv2.IMREAD_COLOR)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Convert to gray

    grid(image_gray, cell_size, gray_window_name)
    grid(image, cell_size, color_window_name)

    cv2.waitKey(0)

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()