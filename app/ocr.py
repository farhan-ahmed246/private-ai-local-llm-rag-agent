def ocr_image(path:str,lang:str='eng')->str:
 from PIL import Image
 import pytesseract
 return pytesseract.image_to_string(Image.open(path),lang=lang)