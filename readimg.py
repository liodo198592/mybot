from PIL import Image
import pytesseract

text = pytesseract.image_to_string(Image.open('out.png'), lang='chi_sim')
print(text)
