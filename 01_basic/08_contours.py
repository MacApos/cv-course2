import cv2

original_img = cv2.imread(r'assets\python.png')
img = original_img.copy()
# cv2.imshow('original_img', img)

gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray', gray)

thresh = cv2.threshold(src=gray, thresh=220, maxval=255, type=cv2.THRESH_BINARY)[1]
# cv2.imshow('thresh', thresh)

contours = cv2.findContours(image=thresh, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)[0]
print(f'Liczba wszysykich konturów: {len(contours)}')

# for contour in contours:
#     index = contours.index(contour)
#     print(index)
#     img_cnt = cv2.drawContours(image=img.copy(), contours=[contours[index]], contourIdx=-1, color=(0, 255, 0),
#                                thickness=2)
#     cv2.imshow(f'img_cnt_{index}', img_cnt)
#     cv2.waitKey(1500)
#     cv2.destroyWindow(f'img_cnt_{index}')

area = cv2.contourArea(contour=contours[4], oriented=True)
# print(area)

max_area = 0
min_area = abs(cv2.contourArea(contour=contours[0], oriented=True))

for idx, contour in enumerate(contours):
    area = cv2.contourArea(contour=contours[idx], oriented=True)
    if area > max_area:
        max_area = area
        max_area_idx = idx
    if abs(area) <= min_area:
        min_area = abs(area)
        min_area_idx = idx

print(f'Największe pole równe: {max_area} ma kontur z indeksem: {max_area_idx}')
print(f'Najmniejsze pole równe: {min_area} ma kontur z indeksem: {min_area_idx}')
max_cnt = cv2.drawContours(image=img.copy(), contours=[contours[max_area_idx]], contourIdx=-1, color=(255, 0, 0),
                           thickness=5)
cv2.imshow('max_cnt', max_cnt)
min_cnt = cv2.drawContours(image=img.copy(), contours=[contours[min_area_idx]], contourIdx=-1, color=(255, 0, 0),
                           thickness=5)
cv2.imshow('min_cnt', min_cnt)
cv2.waitKey(0)

# Długość konturu
perimeter = cv2.arcLength(curve=contours[max_area_idx], closed=True)
print(perimeter)