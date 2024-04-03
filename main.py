import cv2 as cv
import numpy as np

# canvas features :
width = 900
height = 600

# blank image :
img = np.zeros((height, width, 3), dtype= np.uint8)



# draw house no 1:
cv.rectangle(img, (30, 450), (200, 225), (90,20,30), -1)

# draw church :
# x coordinates : 250,325, y = 450 to 200
cv.rectangle(img, (250, 450), (325, 200), (90,20,30), -1)

# church roof (triangle):
church_roof = np.array([[230, 200],[345, 200], [287.5,120]], dtype=np.int32)
cv.fillPoly(img, [church_roof], (90, 20, 30))

# house no 2 :
cv.rectangle(img, (375, 450), (500, 300), (90, 20, 30), -1 )

# draw border of ground :
cv.line(img, (0, 450), (900, 450), (255,255,255), 5)


# draw fence (wide) :
cv.line(img, (0, 400), (900, 400), (100,100,150), 3)
cv.line(img, (0, 425), (900, 425), (100,100,150), 3)

# draw fence sticks :
fence_stick = 10

fence_color = (100, 100, 150)

for fence_stick in range(fence_stick, 900, 20):
    fence_point_1 = (fence_stick, 450)
    fence_point_2 = (fence_stick, 380)
    cv.line(img, fence_point_1, fence_point_2, fence_color, 3)



# draw ground :
cv.rectangle(img, (0, 450), (900, 600), (20, 100, 10), -1)



cv.imshow('Nightscape', img)
cv.waitKey(0)
cv.destroyAllWindows()