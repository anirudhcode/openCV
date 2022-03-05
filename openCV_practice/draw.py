import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), np.dtype('uint8'))


#draw a rectangle
cv.rectangle(blank,(100,100),(400,400),(0,255,0),thickness=5)

cv.imshow('rectangle',blank)


cv.waitKey(0)





#drawing a circle
cv.circle(blank,(250,250),50,(0,0,255),thickness=cv.FILLED)
cv.imshow('circle',blank)

cv.waitKey(0)

#drawing a line
cv.line(blank,(100,100),(250,250),(255,0,0),thickness=5)

cv.imshow('line',blank)

cv.waitKey(0)
cv.destroyAllWindows
#write text on image

blank2 = np.zeros((500,500,3), np.dtype('uint8'))
cv.putText(blank2,'That will be all',(100,100),cv.FONT_HERSHEY_TRIPLEX,1,(255,255,255),thickness=2)
cv.imshow('text',blank2)
cv.waitKey(0)
cv.destroyAllWindows