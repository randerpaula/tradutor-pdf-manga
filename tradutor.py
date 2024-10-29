from translate import Translator

translator= Translator(to_lang="pt")

output = translator.translate(input(str('O que traduzir?')))
print(f'A traducao é {output}')