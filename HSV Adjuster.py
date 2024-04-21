import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow('HSV')

cv2.createTrackbar('HMin', 'HSV', 0, 255, nothing)
cv2.createTrackbar('HMax', 'HSV', 0, 255, nothing)
cv2.createTrackbar('SMin', 'HSV', 0, 255, nothing)
cv2.createTrackbar('SMax', 'HSV', 0, 255, nothing)
cv2.createTrackbar('VMin', 'HSV', 0, 255, nothing)
cv2.createTrackbar('VMax', 'HSV', 0, 255, nothing)

# cam = cv2.VideoCapture('./Videos/Park Video.mp4')

while True:
    # _, image = cam.read()
    image = cv2.imread(r'C:\Users\amary\PycharmProjects\cv for project\Final\test1\2023-10-26 (1).png')

    hMin = cv2.getTrackbarPos('HMin', 'HSV')
    sMin = cv2.getTrackbarPos('SMin', 'HSV')
    vMin = cv2.getTrackbarPos('VMin', 'HSV')

    hMax = cv2.getTrackbarPos('HMax', 'HSV')
    sMax = cv2.getTrackbarPos('SMax', 'HSV')
    vMax = cv2.getTrackbarPos('VMax', 'HSV')

    lower = np.array([hMin, sMin, vMin])
    upper = np.array([hMax, sMax, vMax])

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    masked = cv2.inRange(hsv, lower, upper)
    output = cv2.bitwise_and(image, image, mask= masked)

    cv2.imshow('Image', output)

    if cv2.waitKey(1) == ord('q'):
        break