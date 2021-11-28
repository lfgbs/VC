# ***********************************************************************************
# Name:           chessboard.py
# Revision:
# Date:           28-10-2019
# Author:         Paulo Dias
# Comments:       ChessBoard Tracking
#
# images         left1.jpg->left19.jpg
# Revision:
# Libraries:    Python 3.7.3 + openCV 4.1.0
# ***********************************************************************************
import numpy as np
import cv2
import glob

# Board Size
board_h = 9
board_w = 6

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.


def  FindAndDisplayChessboard(img):
    # Find the chess board corners
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, corners = cv2.findChessboardCorners(gray, (board_w,board_h),None)

    # If found, display image with corners
    if ret == True:
        img = cv2.drawChessboardCorners(img, (board_w, board_h), corners, ret)
        cv2.imshow('img',img)
        cv2.waitKey(100)

    return ret, corners

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((board_w*board_h,3), np.float32)
objp[:,:2] = np.mgrid[0:board_w,0:board_h].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

# Read images
images = glob.glob('images/left*.jpg')

dimensions=None

for fname in images:
    img = cv2.imread(fname)
    dimensions=img.shape[:2]
    ret, corners = FindAndDisplayChessboard(img)
    if ret == True:
        objpoints.append(objp)
        imgpoints.append(corners)


#dimensions=dimensions[::-1]
print(dimensions)

#ret, matriz, distorção, rotacao, translação
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, dimensions, None, None)

print ( " Intrinsics : " )
print ( mtx )
print ( " Distortion : " )
print ( dist )
for i in range ( len ( tvecs ) ) :
    print ( " Translations (% d ) : " % i )
    print ( tvecs [0])
    print ( " Rotation (% d ) : " % i )
    print ( rvecs [0])


index=0
img=cv2.imread(images[index])

print(img)

#projeção cubo em imagem
cubo=np.float32([[0,0,0],[0,0,-1], [1,0,-1], [1,0,0], 
                  [0,1,0], [0,1,-1], [1,1,-1], [1,1,0]]).reshape(-1,3)
point_projection, jac=cv2.projectPoints(cubo, rvecs[index], tvecs[index], mtx, dist)
print("point projection")
print(point_projection)
print(point_projection[0][0])
 
cv2.line(img, tuple(point_projection[0][0]), tuple(point_projection[1][0]), (0,0,255))
cv2.line(img, tuple(point_projection[1][0]), tuple(point_projection[2][0]), (255,0,0))
cv2.line(img, tuple(point_projection[2][0]), tuple(point_projection[3][0]), (0,255,0))

cv2.line(img, tuple(point_projection[0][0]), tuple(point_projection[4][0]), (0,0,255))
cv2.line(img, tuple(point_projection[1][0]), tuple(point_projection[5][0]), (0,0,255))
cv2.line(img, tuple(point_projection[4][0]), tuple(point_projection[5][0]), (0,0,255))

cv2.line(img, tuple(point_projection[5][0]), tuple(point_projection[6][0]), (0,0,255))
cv2.line(img, tuple(point_projection[6][0]), tuple(point_projection[2][0]), (0,0,255))
cv2.line(img, tuple(point_projection[6][0]), tuple(point_projection[7][0]), (0,0,255))

cv2.imshow("image", img)

cv2.waitKey(-1)
np.savez("camera.npz" , intrinsics = mtx , distortion = dist)
cv2.destroyAllWindows()