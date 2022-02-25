import cv2 as cv
import numpy as np
import time

cap = cv.VideoCapture('./videos/clip.mp4')

while True:
    ret,frame = cap.read()
    if ret == False:
        break
    cv.imshow("Video",frame)
    if cv.waitKey(1)==ord('q'):
        break
cap.release()
cv.destroyAllWindows()