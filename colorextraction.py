import cv2
import numpy as np

cap = cv2.VideoCapture(2)

while(1):
    print("hoge")
    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of color in HSV  BGR
    # Bluelow 100.70.70
    # Bluehigh 150.210.210
    # Redlow 0.180.180
    # Redhigh 10.255.255
    # yellowlow 20.130.130
    # yellowhigh 50.255.255
    lower_blue = np.array([100,70,70])
    upper_blue = np.array([150,210,210])

    lower_red = np.array([0,180,180])
    upper_red = np.array([10,255,255])

    lower_yellow = np.array([20,130,130])
    upper_yellow = np.array([50,255,255])


    # Threshold the HSV image to get only blue colors
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # Bitwise-AND mask and original image
    mask_sumRB = cv2.bitwise_or(mask_blue, mask_red)
    mask = cv2.bitwise_or(mask_sumRB, mask_yellow)
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask_blue',mask_blue)
    cv2.imshow('mask_red' ,mask_red)
    cv2.imshow('mask_yellow' ,mask_yellow)
    cv2.imshow('res',res)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cv2.destroyAllWindows()
