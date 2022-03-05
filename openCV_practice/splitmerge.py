from tokenize import blank_re
import cv2 as cv
import numpy as np




img = cv.imread('city2.jpg')
resized = cv.resize(img, (750,550), interpolation=cv.INTER_CUBIC)
cv.imshow('resized',resized)

blank = np.zeros(resized.shape[:2], dtype='uint8')

cv.waitKey(0)

#splitting image into color channels

b,g,r = cv.split(resized)
#printing channels

blue = cv.merge([b,blank,blank])
green = cv.merge((blank,g,blank))
red = cv.merge((blank,blank,r))

cv.imshow('blue',blue)
cv.imshow('green',green)
cv.imshow('red',red)

cv.waitKey(0)

print(resized.shape)
print(b.shape)
print(g.shape)
print(r.shape)


cv.waitKey(0)

#merging color channels

merged = cv.merge((b,g,r))
cv.imshow('merged',merged)

cv.waitKey(0)


cv.destroyAllWindows