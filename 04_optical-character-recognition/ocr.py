import pytesseract
from PIL import Image
import imutils
import cv2


def ocr(filename):
    return pytesseract.image_to_string(image=Image.open(filename))


filename = r'C:\Users\Maciej\PycharmProjects\cv-course2\04_optical-character-recognition\cap_2.png'
img = cv2.imread(filename)

# print(ocr(filename))

cv2.imshow('img', img)
cv2.waitKey(0)