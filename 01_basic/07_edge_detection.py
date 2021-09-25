import cv2
import imutils

img = cv2.imread(r'assets\guido.jpg')
img = imutils.resize(image=img, height=500)
# cv2.imshow('img', img)

canny = cv2.Canny(image=img, threshold1=250, threshold2=250)
# cv2.imshow('canny', canny)

for thresh in range(0,275, 25):
    canny = cv2.Canny(image=img, threshold1=thresh, threshold2=thresh)
    cv2.imshow(f'canny_{thresh}', canny)
    cv2.waitKey(1500)
    cv2.destroyWindow(f'canny_{thresh}')

cv2.waitKey(0)