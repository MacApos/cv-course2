import cv2


def get_position(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f'x={x}, y={y}')


def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(
            img=img,
            center=(x, y),
            radius=50,
            color=(255, 0, 0),
            thickness=5
        )


img = cv2.imread(r'assets\tesla.jpg')

cv2.namedWindow('image')
# cv2.setMouseCallback('image', get_position)

cv2.setMouseCallback('image', draw_circle)

while True:
    cv2.imshow('image', img)
    # Jeżeli będzie wciśnięty ESC wtedy pętla jest przerywana
    if cv2.waitKey(1) == 27:
        break

