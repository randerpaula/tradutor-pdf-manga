from pytesseract import pytesseract
from translate import Translator

translator= Translator(to_lang="pt")
caminho_tesseract = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
pytesseract.tesseract_cmd = caminho_tesseract 

texto = pytesseract.image_to_string("teste4.png")
linhas = texto.split("\n")


#for linha in linhas:
 #   if not linha.isspace() and len (linha) > 0:
  #      print(linha)
print(texto)
print(type(texto))
output = translator.translate(texto)
print(f'A traducao é {output}')
