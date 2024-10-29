import aspose.words as aw
doc = aw.Document("arquivo_traduzido.txt")
doc.save("Output.pdf")
print('Fim da geracao do pdf')