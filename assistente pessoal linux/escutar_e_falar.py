import speech_recognition as sr
from gtts import gTTS
from playsound import playsound





def cria_audio(audio):
	tts = gTTS(audio,lang='pt-br')
	#Salva o arquivo de audio
	tts.save('audios/hello.mp3')
	#print("Estou aprendendo o que você disse...")
	#Da play ao audio
	playsound('audios/hello.mp3')

def ouvir_microfone():
	while True:
		#Habilita o microfone para ouvir o usuario
		microfone = sr.Recognizer()
		with sr.Microphone() as source:
			microfone.adjust_for_ambient_noise(source)
			print("Diga alguma coisa: ")
			audio = microfone.listen(source)                                                                                 #Armazena a informacao de audio na variavel
		try:
			frase = microfone.recognize_google(audio,language='pt-BR')
			print("Você disse: " + frase)

		except sr.UnkownValueError:
			print("Não entendi")
		return frase



frase = ouvir_microfone()
cria_audio('eu te amo')