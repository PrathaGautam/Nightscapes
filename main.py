import cv2 as cv
import numpy as np

# canvas features :
width = 900
height = 600

# blank image :
img = np.zeros((height, width, 3), dtype= np.uint8)


cv.imshow('Nightscape', img)
cv.waitKey(0)
cv.destroyAllWindows()
# draw background :
