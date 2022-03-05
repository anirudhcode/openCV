from cv2 import Canny
import numpy as np
import cv2 as cv

img = cv.imread('city.jpg')
resized = cv.resize(img, (750,620), interpolation=cv.INTER_CUBIC)

cv.imshow('resized',resized)
cv.waitKey(0)

gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
cv.waitKey(0)

#laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('laplacian',lap)

cv.waitKey(0)

#sobel

sobelX = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobelY = cv.Sobel(gray, cv.CV_64F, 0, 1)

combined_sobel = cv.bitwise_or(sobelX, sobelY)

cv.imshow('sobelX',sobelX)
cv.imshow('sobelY',sobelY)


cv.waitKey(0)

cv.imshow('combined_sobel',combined_sobel)
cv.waitKey(0)

canny = cv.Canny(gray, 100, 200)
cv.imshow('canny',canny)

cv.waitKey(0)


cv.destroyAllWindows