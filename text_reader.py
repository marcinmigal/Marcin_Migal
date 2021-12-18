import cv2, pytesseract
import matplotlib.pyplot as plt
pytesseract.pytesseract.tesseract_cmd =r'C:\Program Files\Tesseract-OCR\tesseract'
# pytesseract.pytesseract.tesseract_cmd =r'C:\Program Files\Tesseract-OCR'


img = cv2.imread('photo_5.jpg')

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(pytesseract.image_to_string((img)))


d = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)
n_boxes = len(d['level'])
for i in range(n_boxes):
    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)




