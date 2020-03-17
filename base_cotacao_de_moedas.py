import  requests
import time

def moedas(moeda):
	url = ('https://economia.awesomeapi.com.br/json/all')
	req = requests.get(url, timeout=3000)
	retorno = req.json()
	valores = retorno[moeda]
	conversao = valores['codein']
	data = valores['create_date']
	nome = valores['name']
	valor = valores['ask']
	alta = valores['high']
	baixa = valores['low']
	print(f"""=============================
      COTAÇÃO DE MOEDAS
=============================
Moeda:     {nome}
Conversão: {conversao}
Data:      {data}
Valor:     R${valor}
Alta:      R${alta}USD
Baixa:     R${baixa}
""")
	time.sleep(1)
	print('...')
	time.sleep(2)
	print('......')
	time.sleep(2)


while True:
	moeda = str(input(f"""
========================================================
				   COTAÇÃO DE MOEDAS
========================================================
 [USD]-DolarComercial [USDT]-DolarTurismo [EUR]-Euro
 [ARS]-PesoArgentino  [CAD]DolarCanadense [BTC]Bitcoin        
 [JPY]-Iene Japones   [CNY]-YuanChines    [LTC]LiteCoin
Digite sigla da moeda: """))
	moedas(moeda)