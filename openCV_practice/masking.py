import cv2 as cv
from cv2 import rectangle
import numpy as np

img = cv.imread('city2.jpg')
resized = cv.resize(img, (750,550), interpolation=cv.INTER_CUBIC)

cv.imshow('resized',resized)

cv.waitKey(0)

blank = np.zeros(resized.shape[:2], dtype='uint8')
#cv.imshow('blank',blank)

#Masking
# mask = cv.circle(blank.copy(), (resized.shape[1]//2,resized.shape[0]//2 + 100), 100, 255, -1)

# cv.imshow('mask',mask)

#cv.waitKey(0)

circle = cv.circle(blank.copy(), (200,200), 200, (255,255,255), -1)
rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), (255,255,255), -1)

weird_shape = cv.bitwise_or(circle, rectangle)

cv.imshow('weird_shape',weird_shape)

masked = cv.bitwise_and(resized,resized, mask=weird_shape)
cv.imshow('masked',masked)
cv.waitKey(0)


cv.destroyAllWindows