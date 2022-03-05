import cv2 as cv

#reading images in OpenCV

capture = cv.VideoCapture('video.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('frame', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
