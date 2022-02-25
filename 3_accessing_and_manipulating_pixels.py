import cv2 as cv
import numpy as np

img = cv.imread('./images/bird.jpg')

def display(winname,image):
    cv.imshow(winname,image)
    cv.waitKey(0)
    cv.destroyAllWindows()

# print(type(img))
display('Kingfisher',img)

# accessing first 100 rows & 100 columns

display('Accessed',img[0:100,0:100])

# manipulating with red color

red = (0,0,255)
img[0:100,0:100]=red
display("Manipulated",img)