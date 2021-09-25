import cv2
import numpy as np

original_img = cv2.imread(filename=r'assets/python.png')
img = original_img.copy()

# cv2.imshow(winname='img', mat=img)
# cv2.waitKey(0)

height, width = img.shape[:2]
print(f'Wysokość: {height}')
print(f'Szerokość: {width}')

# Linia
# cv2.line(img=img, pt1=(0, 0), pt2=(width, height), color=(0, 0, 255), thickness=2)
# cv2.imshow(winname='img', mat=img)
# cv2.waitKey(0)

# Prostokąt
# cv2.rectangle(img=img, pt1=(210, 50), pt2=(390, 230), color=(255, 0, 255), thickness=2)
# cv2.imshow(winname='img', mat=img)
# cv2.waitKey(0)

# Okrąg
# cv2.circle(img=img, center=(300, 140), radius=90, color=(0, 0 ,255), thickness=2)
# cv2.imshow(winname='img', mat=img)
# cv2.waitKey(0)

# Otwarty wielokąt
# pts = np.array([[300, 140], [200, 200], [200, 50], [300, 50]], dtype='int32').reshape((-1, 1, 2))
# cv2.polylines(img=img, pts=[pts], isClosed=False, color=(0, 255, 255), thickness=5)
# cv2.imshow('img', img)
# cv2.waitKey(0)

# Zamknięty wielokąt
# pts = np.array([[300, 140], [200, 200], [200, 50], [300, 50]], dtype='int32').reshape((-1, 4, 2))
# cv2.polylines(img=img, pts=[pts], isClosed=True, color=(0, 255, 0), thickness=2)
# cv2.imshow('img', img)
# cv2.waitKey(0)

# Tekst
cv2.putText(img=img,
            text="EloMelo",
            org=(20, 60),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=1.5,
            color=(0, 255, 0),
            thickness=5)
cv2.imshow('img', img)
cv2.waitKey(0)
