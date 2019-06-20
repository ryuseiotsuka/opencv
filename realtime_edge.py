import numpy as np
import cv2

cap = cv2.VideoCapture(2)

while(True):
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame =  cv2.Canny(frame, threshold1 = 100, threshold2=300)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
