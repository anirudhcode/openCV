import cv2 as cv
from cv2 import circle
from cv2 import bitwise_and
from cv2 import bitwise_or
import numpy as np

blank = np.zeros((400,400,3), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), (255,255,255), -1)

circle = cv.circle(blank.copy(), (200,200), 200, (255,255,255), -1)

cv.imshow('rectangle', rectangle)
cv.waitKey(0)

cv.imshow('circle', circle)
cv.waitKey(0)

#BITWISE OPERATIONS
#Bitwise AND

bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('bitwise_and', bitwise_and)

cv.waitKey(0)
#Bitwise OR
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('bitwise_or', bitwise_or)
cv.waitKey(0)

#Bitwise XOR
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('bitwise_xor', bitwise_xor)
cv.waitKey(0)

#Bitwise NOT
bitwise_not = cv.bitwise_not(bitwise_and)
cv.imshow('bitwise_not', bitwise_not)
cv.waitKey(0)

cv.destroyAllWindows