import wikipedia

termo = input('Pesquisa: ')
wikipedia.set_lang("pt")
pesquisa = wikipedia.summary(termo)
print(pesquisa)
