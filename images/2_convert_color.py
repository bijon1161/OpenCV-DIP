import cv2 as cv
img = cv.imread('./images/flemingo.jpg')
b,g,r = cv.split(img)
cv.imshow('color',img)
cv.imshow('blue',b)
cv.imshow('red',r)
cv.imshow('green',g)
cv.waitKey(0)
cv.destroyAllWindows()