import cv2

img = cv2.imread(r'assets\poland.png')
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

gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray', gray)

thresh = cv2.threshold(src=gray, thresh=180, maxval=255, type=cv2.THRESH_BINARY)[1]
# cv2.imshow('thresh', thresh)

contours = cv2.findContours(image=thresh, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)[0]
print(f'Liczba wszystkich konturów: {len(contours)}')

copy = img.copy()
min_area = abs(cv2.contourArea(contour=contours[0], oriented=True))

for idx, cnt in enumerate(contours):
    area = cv2.contourArea(contour=contours[idx], oriented=True)
    if abs(area) <= min_area:
        min_area = abs(area)
        min_area_idx = idx

contour = contours[min_area_idx]
img = cv2.drawContours(image=copy, contours=[contour], contourIdx=-1, color=(0, 255, 255),
                       thickness=5)

# funkcja findContours zwraca listę macierzy tylu rzędach ile jest punktów konturu, 1 kolumni i 2 kanałach x i y
leftmost = contour[contour[:, :, 0].argmin()][0]
rightmost = contour[contour[:, :, 0].argmax()][0]
topmost = contour[contour[:, :, 1].argmin()][0]
bottommost = contour[contour[:, :, 1].argmax()][0]

for point in [leftmost, rightmost, topmost, bottommost]:
    print(tuple(point))
    cv2.circle(img=img, center=tuple(point), radius=10, color=(0, 0, 255), thickness=-1)

cv2.imshow('img', img)
cv2.waitKey(0)
