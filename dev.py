from PyPDF2 import PdfReader
from translate import Translator
from shutil import copyfile
import aspose.words as aw

conteudo = ''

translator= Translator(to_lang="pt")
reader = PdfReader("pdf5.pdf")

pag_conteudo = {}

for indx, pdf_pag in enumerate(reader.pages):
    pag_conteudo[ indx + 1 ] = pdf_pag.extract_text().encode("utf-8")
    
pag_conteudo = str(pag_conteudo).replace("\\n", "").split(".")

for frases in pag_conteudo:
    conteudo = conteudo + translator.translate(frases)+'. '

conteudo = conteudo.replace("{1: b'","").replace("'}.","")
arquivo = open("arquivo_traduzido.txt", "a")
arquivo.write(conteudo)


print('Fim da geração do txt')



