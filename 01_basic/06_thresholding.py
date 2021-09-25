import cv2

img = cv2.imread(r'assets\grey.png')
print(img)
cv2.imshow('img', img)

thresh_binary = cv2.threshold(src=img, thresh=150, maxval=255, type=cv2.THRESH_BINARY)[1]
# cv2.imshow('thresh_binary', thresh_binary)

for thresh in range(50, 250, 50):
    thresh_binary = cv2.threshold(src=img, thresh=thresh, maxval=255, type=cv2.THRESH_BINARY)[1]
    cv2.imshow(f'thresh_binary: {thresh}', thresh_binary)
    cv2.waitKey(2500)
    cv2.destroyWindow(f'thresh_binary: {thresh}')

cv2.waitKey(0)