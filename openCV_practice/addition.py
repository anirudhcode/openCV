#program to demostrate addition of two images using openCV

import cv2
from cv2 import waitKey
from matplotlib.image import imread
import numpy as np

from PIL import Image


path = "D:/Anirudh/sample_images"

image1 = cv2.imread(path +"/cat.jpg",0)
image2 = cv2.imread(path +"/sea.jpg",0)



#cropping image 1
image = image1.open(path+"/cat.jpg")

image_arr = np.array(image)

image = image_arr[700:1400, 1450:2361]

image = image.fromarray(image_arr)

image1 = image


#cropping image 2

image_cr = image.open(path+"/sea.jpg")

image_arr = np.array(image_cr)

image = image_arr[700:1400, 1450:2361]

image = image.fromarray(image_arr)

image2 = image


weightedSum = cv2.addWeighted(image1,0.5,image2,0.5,0)

#displaying the image
cv2.imshow('weighted image', weightedSum)

waitKey(0)

if cv2.waitKey(0) & 0xFF == 0xff == 27:
    cv2.destroyAllWindows()
