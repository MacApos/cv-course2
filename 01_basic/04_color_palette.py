import cv2
import numpy as np


def nothing(x):
    pass


img = np.zeros(shape=(300, 500, 3), dtype='uint8')
cv2.namedWindow('Paleta')

cv2.createTrackbar('Red', 'Paleta', 0, 255, nothing)
cv2.createTrackbar('Green', 'Paleta', 0, 255, nothing)
cv2.createTrackbar('Blue', 'Paleta', 0, 255, nothing)

while True:
    cv2.imshow('Paleta', img)

    r=cv2.getTrackbarPos('Red', 'Paleta')
    g=cv2.getTrackbarPos('Green', 'Paleta')
    b=cv2.getTrackbarPos('Blue', 'Paleta')

    img[:] = [r, g, b]

    if cv2.waitKey(1) == 27:
        break