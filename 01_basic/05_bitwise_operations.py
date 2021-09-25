import cv2
import imutils

img = cv2.imread(r'assets\green_grass.jpg')
logo = cv2.imread(r'assets\jupiter.jpg')
# img = imutils.resize(img, height=750)
logo = imutils.resize(logo, height=400)
# cv2.imshow('image', img)
# cv2.imshow('logo', logo)
cv2.waitKey(0)

rows, col, channels = logo.shape
height, width = [50, 200]
roi = img[height:height+rows, width:width+col]
# cv2.imshow('roi', roi)

gray = cv2.cvtColor(src=logo, code=cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray', gray)

# Threshold zwraca dwa elementy dlatego, trzeba wyciąc jeden z nich – [1]
mask = cv2.threshold(src=gray, thresh=230, maxval=255, type=cv2.THRESH_BINARY)[1]
# cv2.imshow('mask', mask)

mask_inv = cv2.bitwise_not(mask)
# cv2.imshow('mask_inv', mask_inv)

# bg – background
img_bg = cv2.bitwise_and(src1=roi, src2=roi, mask=mask)
logo_fg = cv2.bitwise_and(src1=logo, src2=logo, mask=mask_inv)
# cv2.imshow('img_bg', img_bg)
# cv2.imshow('logo_fg', logo_fg)
dst = cv2.add(img_bg, logo_fg)
img[height:height+rows, width:width+col] = dst
cv2.imshow('img', img)
cv2.waitKey(0)
