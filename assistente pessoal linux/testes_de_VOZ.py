
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

"""Sempre que quisermos falar com nosso sistema poderemos fazer este atraves do speech recognition
instale a lib de acordo com a versao mais recente no site oficial, depois leia atentamente o codigo e os comentarios 
nele contidos"""

def cria_audio(audio):
	"""esta funçao chama o gtts para ler oque voce quiser, pode ser trocada a linguagem  pois ele usa linguagem da google"""
	tts = gTTS(audio,lang='pt-br')
	#Salva o arquivo de audio
	tts.save('audios/hello.mp3')
	#Da play ao audio
	playsound('audios/hello.mp3')


def ouvir_microfone():
	while True:
		#Habilita o microfone para ouvir o usuario
		microfone = sr.Recognizer()
		with sr.Microphone() as source:
			#ajusta o ruido do ambiente para nao ficar dando tanto erro com barulhos obsoletos
			microfone.adjust_for_ambient_noise(source)
			print("Diga alguma coisa: ")
			audio = microfone.listen(source)      #aqui ele escuta oque ta no microfone                                                                           #Armazena a informacao de audio na variavel
		try:
			frase = microfone.recognize_google(audio,language='pt-BR', show_all=False) #grava em uma variavel oque ele ouviu no microfone
			cria_audio(f'você disse {frase}')   #responde via voz com a funçao que definimos acima
			print("Você disse: " + frase)

		except Exception as e: #trata erro em caso de ruidos ou nao reconhecer oque voce disse
			e = '...'
			print(e)
	return frase
frase = ouvir_microfone()


