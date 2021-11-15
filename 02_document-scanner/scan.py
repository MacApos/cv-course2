from skimage.filters import threshold_local
from numpy.linalg import norm
import numpy as np
import argparse
import imutils
import sys
import cv2


def get_perspective(image, contours, ratio):
    points = contours.reshape(4, 2)
    points = points * ratio
    rectangle = np.zeros(shape=(4, 2), dtype='float32')

    total = points.sum(axis=1)
    rectangle[0] = points[np.argmin(total)]
    rectangle[2] = points[np.argmax(total)]

    difference = np.diff(points, axis=1)
    rectangle[1] = points[np.argmin(difference)]
    rectangle[3] = points[np.argmax(difference)]

    [a, b, c, d] = rectangle

    width1 = norm(a-b)
    width2 = norm(c-d)
    max_width = max(int(width1), int(width2))

    height1 = norm(b-c)
    height2 = norm(a-d)
    max_height = max(int(height1), int(height2))

    destination = np.array([[0, 0],
                            [max_width-1, 0],
                            [max_width-1, max_height-1],
                            [0, max_height-1],
                            ], dtype='float32')

    M = cv2.getPerspectiveTransform(src=rectangle, dst=destination)
    warped_image = cv2.warpPerspective(src=image, M=M, dsize=(max_width, max_height))
    return warped_image


ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='path to image')
args = vars(ap.parse_args())

print(f'Numpy version: {np.__version__}')
print(f'OpenCV version: {cv2.__version__}')

# Wczytywanie obrazu
image = cv2.imread(r'C:\Users\Maciej\PycharmProjects\cv-course2\01_basic\assets\paragon_1.jpg')
original_image = image.copy()
ratio = image.shape[0] / 500.0
image = imutils.resize(image, height=500)

gray = cv2.cvtColor(src=image, code=cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(src=gray, ksize=(5, 5), sigmaX=0)

edges = cv2.Canny(image=blurred, threshold1=70, threshold2=200)

contours = cv2.findContours(image=edges, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:5]

detected_contour = None

for idx, contour in enumerate(contours):
    perimeter = cv2.arcLength(curve=contour, closed=True)
    approx = cv2.approxPolyDP(curve=contour, epsilon=0.02 * perimeter, closed=True)

    if len(approx) == 4:
        print('Można przetowrzyć obraz')
        detected_contour = approx
        break

if not isinstance(detected_contour, np.ndarray):
    print('Nie można przetowrzyć obrazu')
    sys.exit(1)

vertices = cv2.drawContours(image=image.copy(), contours=[detected_contour], contourIdx=-1,
                            color=(0, 255, 255), thickness=5)

# Ekstrakcja perspektywy
warped_image = get_perspective(original_image, detected_contour, ratio)

out = cv2.cvtColor(src=warped_image, code=cv2.COLOR_BGR2GRAY)

# Obliczenie maski progowej na podstawie podobieństwa pikseli
T = threshold_local(image=out, block_size=11, method='gaussian', offset=10)
out = (out > T).astype('uint8') * 255
cv2.imshow('res', out)
cv2.waitKey(0)
