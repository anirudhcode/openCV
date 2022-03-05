import cv2 as cv
from cv2 import imshow

import numpy as np

img = cv.imread('lake.jpg')

cv.imshow('frame', img)

cv.waitKey(0)


#resizing an image

def rescaleFrame(frame, scale=2.5):
    width = int(frame.shape[1] * scale)  #width of the frame
    height = int(frame.shape[0] * scale) #height of the frame
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


resized_img = rescaleFrame(img)

cv.imshow('frame2', resized_img)

cv.waitKey(0)

#resizing video file

#reading video file

#resizing video

capture = cv.VideoCapture('video.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=0.2)

    cv.imshow('frame', frame)


    cv.imshow('frame2', frame_resized)


    if cv.waitKey(20) & 0xFF == ord('d'):
        break

cv.waitKey(0)


cv.destroyAllWindows()

#method 2 for resizing video
#only works on live video

#def changeRes(width,height):
 #   capture.set(3,width)
  #  capture.set(4,height)