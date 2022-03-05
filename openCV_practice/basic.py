import cv2 as cv

img = cv.imread('fbd.jpg')

cv.imshow('image',img)

cv.waitKey(0)

 #converting image to grayscale
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# cv.imshow('gray',gray)
# cv.waitKey(0)

#blurring an image
blur = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)
cv.waitKey(0)

# Edge Cascade
canny = cv.Canny(blur,100,200)
cv.imshow('canny',canny)
cv.waitKey(0)

#dilating the image

dilated = cv.dilate(canny,(3,3),iterations=3)
cv.imshow('dilated',dilated)

cv.waitKey(0)

#eroding the image
eroded = cv.erode(dilated,(3,3),iterations=3)
cv.imshow('eroded',eroded)

cv.waitKey(0)

#resizing the image
resized = cv.resize(img,(500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized',resized)
cv.waitKey(0)

#cropping the image
cropped = resized[50:200,200:400]
cv.imshow('cropped',cropped)
cv.waitKey(0)
cv.destroyAllWindows