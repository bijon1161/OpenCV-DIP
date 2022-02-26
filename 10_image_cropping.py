import cv2 as cv
import numpy as np

img = cv.imread('./images/bird.jpg')

def display(winname,image):
    cv.imshow(winname,image)
    cv.waitKey(0)
    cv.destroyAllWindows()

crop = img[100:550,100:450]
display("Cropped Image",crop)