import numpy as np
import cv2 as cv

img = cv.imread('./images/flemingo.jpg')

cv.imshow('This is a Bird',img)
cv.waitKey(0)
cv.imwrite('./images/flamingo.png',img)