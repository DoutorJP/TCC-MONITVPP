import pytesseract
import cv2

imagem = cv2.imread("img.png")

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\Tesseract.exe"

texto = pytesseract.image_to_string(imagem, lang="eng")
print(texto)
if texto[4].isalpha() == True:
    print("Placa Mercosul")
elif texto[4].isnumeric() == True:
    print("Placa Antiga")
else:
    print("Placa não reconhecida.")
