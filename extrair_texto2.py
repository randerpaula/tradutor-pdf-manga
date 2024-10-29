import cv2
import pytesseract as pt

pt.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

img = cv2.imread('teste2.png')

#print(pt.pytesseract.image_to_string(img))
boxes = pt.pytesseract.image_to_boxes(img)
dados = pt.pytesseract.image_to_data(img)
imH, imW,_ = img.shape



for x,linha in enumerate(dados.splitlines()):
    if x!=0:
        linha = linha.split()
        print(linha)
        if len(linha)==12:
            x,y,w,h = int(linha[6]), int(linha[7]), int(linha[8]), int(linha[9])
            palavra=linha[11]
            cv2.rectangle(img,(x,y),(w+x, h+y), (0,0,255),1)
            cv2.putText(img, palavra,(x, y+100),cv2.FONT_HERSHEY_SIMPLEX,1,(8,8,2555),2)

cv2.imshow('Imagem',img)

cv2.waitKey(0)