import cv2
import imutils

img1 = cv2.imread(r'C:\Users\Maciej\PycharmProjects\cv-course2\01_basic\assets\view.jpg')
img2 = cv2.imread(r'C:\Users\Maciej\PycharmProjects\cv-course2\01_basic\assets\python.png')
# img1 = imutils.resize(img1, height=750)
img2 = imutils.resize(img2, height=150)
# cv2.imshow('img1', img1)
# cv2.imshow('img2', img2)

img2shape = img2.shape
roi = img1[:img2shape[0], 0:img2shape[1]]
# cv2.imshow('roi', roi)

# Planeta w skali szarości
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
# Maska planety
mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY)[1]
# Odwrócona maska planety
mask_inv = cv2.bitwise_not(mask)
cv2.imshow('gray', img2gray)
cv2.imshow('mask', mask)
cv2.imshow('mask_inv', mask_inv)

# Zaciemnienie konturu planety na pierwszym planie
img1_bg = cv2.bitwise_and(roi, roi, mask)
cv2.imshow('img1_bg', img1_bg)

# Zaciemnienie tła planety
img2_fg = cv2.bitwise_and(img2, img2, mask_inv)
# cv2.imshow('img2_fg', img2_fg)

dst = cv2.add(img1_bg, img2_fg)
img1[:img2shape[0], :img2shape[1]] = dst
# cv2.imshow('dst', dst)

cv2.waitKey(0)