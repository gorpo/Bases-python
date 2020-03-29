import requests

def previsaoTempo():
	cidade = 'garopaba'
	try:
		url = 'https://api.hgbrasil.com/weather'
		key = 'f21c10a6'
		fields = "only_results,temp,city_name,forecast,max,min,date"
		data = {'key': key, 'fields': fields, 'city_name': cidade}
		req = requests.get(url, data=data, timeout=3000)
		json = req.json()
		print(f"Cidade:{json['city_name']}")
		print(f"Temperatura:{json['temp']}")
		print(f"Data:{json['forecast'][0]['date']}")
		print(f"Min:{json['forecast'][0]['min']}")
		print(f"Max:{json['forecast'][0]['max']}")
		result_audio = f"Temperatura para {json['city_name']} é, {json['temp']} graus, com mínima de {json['forecast'][0]['min']} e máxima de {json['forecast'][0]['max']}"
		print(result_audio)
		cria_audio(result_audio)
	except:
		return "Não foi possivel obter a previsão do tempo tente mais tarde"

while True:
    previsaoTempo()