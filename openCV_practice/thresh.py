import cv2 as cv
from cv2 import threshold


img = cv.imread('city2.jpg')
resized  = cv.resize(img, (750,650), interpolation=cv.INTER_CUBIC)
cv.imshow('resized',resized)

cv.waitKey(0)

gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

cv.waitKey(0)

#simple thresholding
threshold, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('thresh',thresh)
cv.waitKey(0)

threshold, thresh_inv = cv.threshold(gray, 125, 255, cv.THRESH_BINARY_INV)
cv.imshow('thresh_inv',thresh_inv)
cv.waitKey(0)

#Adaptive thresholding

adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
cv.imshow('adaptive_thresh',adaptive_thresh)
cv.waitKey(0)

adaptive_thresh_inv = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 2)
cv.imshow('adaptive_thresh_inv',adaptive_thresh_inv)
cv.waitKey(0)


cv.destroyAllWindows