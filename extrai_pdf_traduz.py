from PyPDF2 import PdfReader
from translate import Translator

translator= Translator(to_lang="pt")
reader = PdfReader("pdf3.pdf")

pag_conteudo = {}

for indx, pdf_pag in enumerate(reader.pages):
    pag_conteudo[ indx + 1 ] = pdf_pag.extract_text()
    

print(pag_conteudo)
output = str(pag_conteudo)
output = translator.translate(output)
print(f'A traducao é {output}')

arquivo = open("arquivo_traduzido.txt", "a")
arquivo.write(output)
