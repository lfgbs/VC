import cv2
import numpy as np
from imutils.video import VideoStream

# Board Size
board_h = 9
board_w = 6

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((board_w*board_h,3), np.float32)
objp[:,:2] = np.mgrid[0:board_w,0:board_h].T.reshape(-1,2)

capture = cv2.VideoCapture(0)

with np.load('camera.npz') as params:
    intrinsics= params["intrinsics"]
    distortion=params["distortion"]

#print(intrinsics, distortion)

while True:
    ret, frame= capture.read()

    frame = cv2.flip(frame, 1) # the second arguments value of 1 indicates that we want to flip horizontally

    ret, corners = cv2.findChessboardCorners(frame, (board_w,board_h),None)

    if ret == True:
        #Como estamos a fazer frame a frame, não há necessidade de criar os arrays objpoints e imgpoints, pode-se passar logo os valores encontrados para cada frame
        ret, rvec, tvec = cv2.solvePnP(objp, corners ,intrinsics, distortion)

        #projeção cubo em imagem
        cubo=np.float32([[0,0,0],[0,0,-1], [1,0,-1], [1,0,0], 
                        [0,1,0], [0,1,-1], [1,1,-1], [1,1,0]]).reshape(-1,3)
    
        point_projection, jac=cv2.projectPoints(cubo, rvec, tvec, intrinsics, distortion)
        
        cv2.line(frame, tuple(point_projection[0][0]), tuple(point_projection[1][0]), (0,0,255))
        cv2.line(frame, tuple(point_projection[1][0]), tuple(point_projection[2][0]), (255,0,0))
        cv2.line(frame, tuple(point_projection[2][0]), tuple(point_projection[3][0]), (0,255,0))

        cv2.line(frame, tuple(point_projection[0][0]), tuple(point_projection[4][0]), (0,0,255))
        cv2.line(frame, tuple(point_projection[1][0]), tuple(point_projection[5][0]), (0,0,255))
        cv2.line(frame, tuple(point_projection[4][0]), tuple(point_projection[5][0]), (0,0,255))

        cv2.line(frame, tuple(point_projection[5][0]), tuple(point_projection[6][0]), (0,0,255))
        cv2.line(frame, tuple(point_projection[6][0]), tuple(point_projection[2][0]), (0,0,255))
        cv2.line(frame, tuple(point_projection[6][0]), tuple(point_projection[7][0]), (0,0,255))

    cv2.imshow('video', frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

capture.release()
cv2.destroyAllWindows()