import numpy as np
import cv2

cam = cv2.VideoCapture(0)
kernel = np.ones((5,5))

while(True):
    
    ret, frame = cam.read()

    hsvframe = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower = np.array([29, 86, 6])
    upper = np.array([100, 255, 255])
   
    mask = cv2.inRange(hsvframe, lower, upper)
    openingmask = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)

    im2,cnts,hierarchy = cv2.findContours(openingmask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
   
    C_max = max(cnts,key=cv2.contourArea)
    
    rect = cv2.minAreaRect(C_max)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    cv2.drawContours(frame,[box],0,(255,255,255),2)
   
    cv2.imshow('output',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
