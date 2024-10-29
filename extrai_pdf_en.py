from PyPDF2 import PdfReader
from translate import Translator

translator= Translator(to_lang="en")
reader = PdfReader("pdf_br.pdf")

pag_conteudo = {}

for indx, pdf_pag in enumerate(reader.pages):
    pag_conteudo[ indx + 1 ] = pdf_pag.extract_text()
    

print(pag_conteudo)
output = str(pag_conteudo)
output = translator.translate(output)
print(f'Translate -> {output}')

arquivo = open("arquivo_traduzido2.txt", "a")
arquivo.write(output)