import cv2 as cv
from cv2 import circle
from matplotlib.pyplot import gray
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('city.jpg')
resized = cv.resize(img, (750,550), interpolation=cv.INTER_CUBIC)

blank = np.zeros(resized.shape[:2], dtype='uint8')

cv.imshow('resized',resized)

cv.waitKey(0)

# gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
# cv.imshow('gray',gray)

# cv.waitKey(0)

mask = cv.circle(blank,(resized.shape[1]//2,resized.shape[0]//2), 100, 255, -1)

masked = cv.bitwise_and(resized, resized, mask=mask)

cv.imshow('mask',masked)

cv.waitKey(0)
#Grayscale histogram
# gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256])
# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.xlabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()
# cv.waitKey(0)

#color histogram
colors = ['b','g','r']
for i,col in enumerate(colors):
    hist = cv.calcHist([resized], [i], mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.title('Color Histogram')
    plt.xlabel('Bins')
    plt.ylabel('# of pixels')
    plt.plot(hist, color=col)
    plt.xlim([0,256])
plt.show()

cv.waitKey(0)
cv.destroyAllWindows