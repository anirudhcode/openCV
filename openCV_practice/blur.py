#SMOOTHING AND BLUR AN IMAGE
import cv2 as cv
import numpy as np

img = cv.imread('city2.jpg')
resized = cv.resize(img, (750,550), interpolation=cv.INTER_CUBIC)
cv.imshow('resized',resized)

cv.waitKey(0)

# averaging
average = cv.blur(resized,(5,5))
cv.imshow('average',average)

cv.waitKey(0)

#Gaussian Blur

gauss = cv.GaussianBlur(resized,(5,5),0)
cv.imshow('gauss',gauss)

cv.waitKey(0)

#Median Blur

median = cv.medianBlur(resized,5)
cv.imshow('median',median)
cv.waitKey(0)

#Bilateral Blur
bilateral = cv.bilateralFilter(resized,5,125,125)
cv.imshow('bilateral',bilateral)

cv.waitKey(0)
cv.destroyAllWindows