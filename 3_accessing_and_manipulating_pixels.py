import cv2 as cv
import numpy as np

img = cv.imread('./images/bird.jpg')

def display(winname,image):
    cv.imshow(winname,image)
    cv.waitKey(0)
    cv.destroyAllWindows()

print(type(img))
display('Kingfisher',img)