import subprocess
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import requests
import webbrowser
import time
import random

def ouvir_microfone():
	while True:
		#Habilita o microfone para ouvir o usuario
		microfone = sr.Recognizer()
		with sr.Microphone() as source:
			microfone.adjust_for_ambient_noise(source)
			print("Diga alguma coisa: ")
			audio = microfone.listen(source)                                                                                 #Armazena a informacao de audio na variavel
		try:
			frase = microfone.recognize_google(audio,language='pt-BR', show_all=False)
			#print(frase)

			#python search-------
			#corona virus---------
			if  'corona' in frase:
				coronaVirus()
			#python libs ---------
			if 'Python' in frase:
				pythonLibs()

			# hora e data-------------------
			if 'horário' in frase:
				hora()
			if 'data' in frase:
				data()
			#noticias-----
			if 'notícias' in frase:
				noticias()
			#gato -- fotos de gato
			if 'gato' in frase:
				gato()
			# pesquisa Google------------
			if 'Google'  in frase:
				pesquisaGoogle(frase)
			# pesquisa Google------------
			if 'YouTube' in frase:
					pesquisaYoutube(frase)
			# previsão do tempo --------------
			if 'clima' in frase:
				previsaoTempo(frase)
			#abre navegador
			if 'Firefox' in frase:
				cria_audio(f'você disse {frase}')
				print("Você disse: " + frase)
				subprocess.call('firefox')
			#calculadora -------------------
			if '+' or '-' in frase:
				calculadora(frase)
			if frase.split(' x ')[1].isnumeric():
				calculadora(frase)
			if frase.split(' / ')[1].isnumeric():
				calculadora(frase)


		except Exception as e:
			e = '...'
			print(e)
	return frase




def pythonLibs():
	nome_lib = str(input('Digite o nome da lib >>> '))
	url = (f'https://pypi.org/pypi/{nome_lib}/json')
	req = requests.get(url, timeout=3000)
	retorno = req.json()
	info = retorno['info']
	print(info)
	print(f"""Autor: {info['author']}
Url: {info['package_url']}""")
	cria_audio(f"""Autor: {info['author']}
Url: {info['package_url']}""")



def coronaVirus():
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
	print('Nomes dos paises para por no Script>>> https://pomber.github.io/covid19/timeseries.json')
	cria_audio(f"""Pais: {pais}
Data: {info['date']}
Confirmados: {info['confirmed']}
Mortos: {info['deaths']}
Recuperados: {info['recovered']}""")


def cria_audio(audio):
	tts = gTTS(audio,lang='pt-br')
	#Salva o arquivo de audio
	tts.save('audios/hello.mp3')
	#print("Estou aprendendo o que você disse...")
	#Da play ao audio
	playsound('audios/hello.mp3')

def pesquisaGoogle(frase):
	texto = frase.split()[1]
	url = 'https://www.google.com/search?q='
	search_url = url + texto
	print(search_url)
	cria_audio('Encontramos seus resultados')
	webbrowser.open_new_tab(search_url)
	time.sleep(2)

def pesquisaYoutube(frase):
	texto = frase.split()[1]
	url = 'https://www.youtube.com/results?search_query='
	search_url = url + texto
	print(search_url)
	cria_audio('Encontramos seus resultados')
	webbrowser.open(search_url)
	time.sleep(2)

def calculadora(frase):
	frase.replace(' ', '')
	if '+' in frase:
		s1 = int(frase.split('+')[0])
		s2 = int(frase.split('+')[1])
		calcs = s1 + s2
		fala_calcs = str(calcs)
		print(f'{frase} = {fala_calcs}')
		cria_audio(f'{frase} é {fala_calcs}')
	elif '-' in frase:
		su1 = int(frase.split('-')[0])
		su2 = int(frase.split('-')[1])
		calcsu = su1 - su2
		fala_calcsu = str(calcsu)
		print(f'{frase} = {fala_calcsu}')
		cria_audio(f'{frase} é {fala_calcsu}')
	elif 'x' in frase:
		m1 = int(frase.split(' x ')[0])
		m2 = int(frase.split(' x ')[1])
		calcm = m1 * m2
		fala_calcm = str(calcm)
		print(f'{frase} = {fala_calcm}')
		cria_audio(f'{frase} é {fala_calcm}')
	elif '/' in frase:
		d1 = int(frase.split(' / ')[0])
		d2 = int(frase.split(' / ')[1])
		calcd = d1 * d2
		fala_calcd = str(calcd)
		print(f'{frase} = {fala_calcd}')
		cria_audio(f'{frase} é {fala_calcd}')

def previsaoTempo(frase):
	cidade = frase.split()[1]
	try:
		url = 'https://api.hgbrasil.com/weather'
		key = '0418e7f0'
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

def noticias():
	url = ('https://newsapi.org/v2/top-headlines?'
		   'country=br&'
		   'apiKey=05d5ce74721c41698d58009213297db9')
	req = requests.get(url, timeout=3000)
	json = req.json()
	# PERCORRENDO AS 10 PRIMEIRAS NOTÍCIAS
	for c in range(10):
		print('Notícia ' + str(c + 1))
		cria_audio('Notícia ' + str(c + 1))
		print(json['articles'][c]['title'])
		cria_audio(json['articles'][c]['title'])
		print(json['articles'][c]['description'])
		cria_audio(json['articles'][c]['description'])

def gato():
	text = 'cat'
	url = (f'https://coub.com/api/v2/search/coubs?q={text}')
	req = requests.get(url, timeout=3000)
	rjson = req.json()
	content = random.choice(rjson['coubs'])
	links = content['permalink']
	print(f'https://coub.com/v/{links}')
	#cria_audio('Encontramos seus resultados')
	webbrowser.open_new_tab(f'https://coub.com/v/{links}')
	time.sleep(2)

def hora():
	t = time.localtime()
	print('Agora são {}:{}:{} e você pode morrer a qualquer momento!'.format(t[3], t[4], t[5]))
	cria_audio('Agora são {}:{}:{} e você pode morrer a qualquer momento!'.format(t[3], t[4], t[5]))

def data():
	t = time.localtime()
	print('Hoje é  {}/{}/{} e faltam poucos dias para começar a guerra!'.format(t[2],t[1],t[0]))
	cria_audio('Hoje é  {}/{}/{} e faltam poucos dias para começar a guerra!'.format(t[2],t[1],t[0]))


frase = ouvir_microfone()


