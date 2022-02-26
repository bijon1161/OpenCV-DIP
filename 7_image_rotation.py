import cv2 as cv
import numpy as np

img = cv.imread('./images/bird.jpg')

def display(winname,image):
    cv.imshow(winname,image)
    cv.waitKey(0)
    cv.destroyAllWindows()

def rotate(image, angle, scale):
    center = (image.shape[1]//2,image.shape[0]//2)
    M = cv.getRotationMatrix2D(center,angle,scale)
    rotate_img = cv.warpAffine(image,M,(image.shape[1],image.shape[0]))
    display("Rotating Image",rotate_img)

rotate(img, 45, .5)