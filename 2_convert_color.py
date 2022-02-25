import cv2 as cv
img = cv.imread('./images/flemingo.jpg')
b,g,r = cv.split(img)
img_rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow('color_bgr',img)
cv.imshow('color_rgb',img_rgb)
cv.imshow('gray',img_gray)

cv.imwrite('./images/grayFlemingo.png',img_gray)
cv.waitKey(0)
cv.destroyAllWindows()