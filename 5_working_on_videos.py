import cv2 as cv
import numpy as np
import time

cap = cv.VideoCapture('./videos/clip.mp4')
fps = 0

while True:
    start_time = time.time()
    ret,frame = cap.read()
    if ret == False:
        break
    
    cv.putText(frame,'FPS :{:.0f}'.format(fps),(30,40),cv.FONT_HERSHEY_SIMPLEX,1.5,(255,255,255),1)
    cv.imshow("Video",frame)
    if cv.waitKey(40)==ord('q'):
        break
    time_taken = time.time() - start_time
    fps = 1/time_taken
cap.release()
cv.destroyAllWindows()