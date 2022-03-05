#Face detection using OpenCV

import cv2 as cv

#img = cv.imread('people.jpg')
img = cv.imread('boys.jpg')
resized = cv.resize(img, (800, 600))

cv.imshow('Original', resized)
cv.waitKey(0)


gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

cv.waitKey(0)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3)


print(f'Number of faces found = {len(face_rect)}')


for (x, y, w, h) in face_rect:
    cv.rectangle(resized, (x, y), (x+w, y+h), (0, 255, 0), 2)


cv.imshow('Faces found', resized)
cv.waitKey(0)

cv.destroyAllWindows