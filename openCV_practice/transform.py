from turtle import width
import cv2 as cv
import numpy as np

img = cv.imread('fbd.jpg')

resized = cv.resize(img,(500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized',resized)

cv.waitKey(0)
#translation

def translate(image,x,y):
    rows,cols,channels = image.shape
    M = np.float32([[1,0,x],[0,1,y]])
    dimensions = (resized.shape[1],resized.shape[0])
    return cv.warpAffine(image,M,dimensions)

translated = translate(resized,100,100)

cv.imshow('translated',translated)
cv.waitKey(0)

#rotation
def rotate(img, angle, rotPoint = None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions = (width, height)

    return cv.warpAffine(img,rotMat, dimensions)

rotated_image = rotate(resized,45)
cv.imshow('rotated',rotated_image)
cv.waitKey(0)

#flipping an image
flipped = cv.flip(resized, -1)
cv.imshow('flipped',flipped)
cv.waitKey(0)

cv.destroyAllWindows