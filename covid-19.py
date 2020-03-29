import requests

pais = 'Brazil'
url = ('https://pomber.github.io/covid19/timeseries.json')
req = requests.get(url, timeout=3000)
retorno = req.json()
dicionario = retorno[pais]
info = dicionario[-1]
print(f"""Pais: {pais}
Data: {info['date']}
Confirmados: {info['confirmed']}
Mortos: {info['deaths']}
Recuperados: {info['recovered']}""")
	#print('Nomes dos paises para por no Script>>> https://pomber.github.io/covid19/timeseries.json')
