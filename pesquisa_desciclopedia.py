import desciclopedia

pesquisa = input('Pesquisar: ')
pesquisar = desciclopedia.search(pesquisa)
retorno = desciclopedia.page(pesquisar[0])
print(retorno.title)
print(retorno.url)
print(retorno.content)

