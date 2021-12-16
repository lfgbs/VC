import cv2
import numpy as np
from functools import partial

def onMouse(event, x, y, flags, params, undistorted_right, width, F):
    if event==cv2.EVENT_LBUTTONDOWN:
        p=np.array([x,y])
    
        epilineR=cv2.computeCorrespondEpilines(p.reshape(-1,1,2),1,F) #returns coeficients of the epipolar line for a given point
        epilineR=epilineR.reshape(-1,3)[0]

        color = np.random.randint(0,255,3).tolist()

        start_point_y=int(-epilineR[2]/epilineR[1]) #simpler because x is 0
        end_point_y=int(-((epilineR[0]*width+epilineR[2])/epilineR[1]))

        cv2.line(undistorted_right, (0, start_point_y), (width, end_point_y), color, 1)
        cv2.imshow("undistorted right", undistorted_right)
        

def main():
    with np.load('stereoParams.npz') as params:
        intrinsics_left= params["intrinsics1"]
        distortion_left=params["distortion1"]
        intrinsics_right= params["intrinsics2"]
        distortion_right=params["distortion2"]
        R= params["R"]
        T=params["T"]
        E= params["E"]
        F=params["F"]

    left_image = cv2.imread('../P5/images/left01.jpg')
    right_image = cv2.imread('../P5/images/right01.jpg')

    h,w=left_image.shape[:2]

    left_image_undistorted=cv2.undistort(left_image, intrinsics_left, distortion_left, None)
    right_image_undistorted=cv2.undistort(right_image, intrinsics_right, distortion_right, None)

    cv2.imshow("undistorted left", left_image_undistorted)
    cv2.imshow("undistorted right", right_image_undistorted)

    cv2.setMouseCallback("undistorted left", partial(onMouse, undistorted_right=right_image_undistorted, width=w, F=F))

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()