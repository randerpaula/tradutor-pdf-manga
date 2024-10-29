from PyPDF2 import PdfReader

reader = PdfReader("pdf3.pdf")

pag_conteudo = {}

for indx, pdf_pag in enumerate(reader.pages):
    pag_conteudo[ indx + 1 ] = pdf_pag.extract_text()
    


print(pag_conteudo)

       






