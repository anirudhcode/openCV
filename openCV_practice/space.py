import cv2 as cv
from matplotlib.pyplot import gray
import matplotlib.pyplot as plt

img = cv.imread('city2.jpg')

resized = cv.resize(img, (850,600), interpolation=cv.INTER_CUBIC)
cv.imshow('resized',resized)

cv.waitKey(0)

# plt.imshow(resized)
# plt.show()

# cv.waitKey(0)

#BGR to grayscale
gray = cv.cvtColor(resized,cv.COLOR_BGR2GRAY)

cv.imshow('gray',gray)

cv.waitKey(0)

#BGR to HSV
hsv = cv.cvtColor(resized,cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)

cv.waitKey(0)

#BGR to LAB
lab = cv.cvtColor(resized,cv.COLOR_BGR2LAB)
cv.imshow('lab',lab)

cv.waitKey(0)

#BGR to RGB
rgb = cv.cvtColor(resized,cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)

# plt.imshow(rgb)
# plt.show()



cv.waitKey(0)

#Grayscale to BGR
bgr_img = cv.cvtColor(gray,cv.COLOR_GRAY2BGR)
cv.imshow('bgr', bgr_img)
cv.waitKey(0)


cv.destroyAllWindows