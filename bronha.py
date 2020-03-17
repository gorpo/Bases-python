import  requests
import webbrowser

def bronha(pesquisa):
	pesquisar = pesquisa.replace(' ','+')
	url = (f'https://xvideos-random-api.herokuapp.com/search?search_description={pesquisar}')
	req = requests.get(url, timeout=3000)
	retorno = req.json()
	titulo = retorno['title']
	url = retorno['url']
	link = f'https://xvideos.com{url}'
	print(f"""Titulo: {titulo}
Link: {link}""")
	webbrowser.open(link)

pesquisa = str(input('Bronha aleatoria: '))
bronha(pesquisa)