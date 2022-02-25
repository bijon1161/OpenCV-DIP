import cv2 as cv
import numpy as np

img = cv.imread('./images/bird.jpg')

def display(winname,image):
    cv.imshow(winname,image)
    cv.waitKey(1)
    cv.destroyAllWindows()


def translation(image,tx,ty):
    M = np.float32([[1,0,tx],
    [0,1,ty]])
    shifted_img = cv.warpAffine(image,M,(image.shape[1],image.shape[0]))
    display("Shifted image",shifted_img)

translation(img,100,150)