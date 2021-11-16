import numpy as np
import cv2
import argparse

def main():

    capture = cv2.VideoCapture(0)

    while True:
        ret, frame= capture.read()
        cv2.imshow('video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        canny=cv2.Canny(frame, 100, 75)
        #canny=cv2.Canny(frame, 1, 255)
        #canny=cv2.Canny(frame, 220, 255)

        cv2.imshow('original', frame)
        cv2.imshow('canny', canny)

    capture.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()