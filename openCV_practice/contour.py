import cv2 as cv
from matplotlib.pyplot import gray
import numpy as np

img = cv.imread('city2.jpg')

#resize image
img = cv.resize(img, (0,0), fx=0.15, fy=0.15)
cv.imshow('Original', img)

cv.waitKey(0)

blank = np.zeros(img.shape, dtype='uint8')
# cv.imshow('blank', blank)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

cv.waitKey(0)

# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('blur', blur)

# cv.waitKey(0)

canny = cv.Canny(img, 125,125)
cv.imshow('canny',canny)
cv.waitKey(0)

#finding contours

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)

cv.imshow('thresh', thresh)

cv.waitKey(0)

contours, hierarchies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found.')

cv.waitKey(0)

#drawing contours

cv.drawContours(blank, contours, -1,(0,0,255), thickness=1)
cv.imshow('contoursDrawn',blank)
cv.waitKey(0)
cv.destroyAllWindows