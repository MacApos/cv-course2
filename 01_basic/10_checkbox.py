import cv2
import numpy as np

img = cv2.imread(r'assets\checkbox.png')
# cv2.imshow('img', img)

img = cv2.copyMakeBorder(
    src=img,
    top=20,
    bottom=20,
    left=20,
    right=20,
    borderType=cv2.BORDER_CONSTANT,
    value=(255, 255, 255)
)

# cv2.imshow('img_bg', img)

gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray', gray)

blurred = cv2.GaussianBlur(src=gray, ksize=(5,5), sigmaX=0)
# cv2.imshow('blurred', blurred)

thresh = cv2.threshold(src=blurred, thresh=75, maxval=200, type=cv2.THRESH_BINARY)[1]
# cv2.imshow('thresh', thresh)

contours = cv2.findContours(image=thresh, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)[0]
print(f'Liczba konturów: {len(contours)}')

img_cnt = cv2.drawContours(image=img.copy(), contours=[contours[2]], contourIdx=-1, color=(0, 255, 0),
                           thickness=5)

# cv2.imshow('img_cnt', img_cnt)

checked_idx = None
total = 0

for idx in [1, 2]:
    # Wygenerowanie maski (kontur z -1 daje pełne pole)
    mask = np.zeros(shape=gray.shape, dtype='uint8')
    cv2.drawContours(image=mask, contours=[contours[idx]], contourIdx=-1, color=255, thickness=-1)
    # cv2.imshow(f'mask {idx}', mask)

    # Odwrotna maska
    mask_inv = cv2.bitwise_not(mask)
    # cv2.imshow(f'mask_inv {idx}', mask_inv)

    # Połączenie maske daje jedno pole dla każdej opcji
    answer = cv2.add(gray, mask_inv)
    # cv2.imshow(f'answer {idx}', answer)

    answer_inv = cv2.bitwise_not(answer)
    # cv2.imshow(f'answer_inv {idx}', answer_inv)

    # Obraz na którym jest mniej  czarnych pikseli (równych 0) jest zaznaczony
    cnt = cv2.countNonZero(answer_inv)
    if cnt > total:
        checked_idx = idx
print(checked_idx)

checked_contour = cv2.drawContours(image=img.copy(), contours=[contours[checked_idx]], contourIdx=-1, color=(0, 255, 0),
                                   thickness=5)
cv2.imshow('checked_contour', checked_contour)
cv2.waitKey(0)