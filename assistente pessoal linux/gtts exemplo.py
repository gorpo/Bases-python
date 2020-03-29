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


frase = 'ola mundo queria falar para voces que sao tudo pau no cu'
cria_audio(frase)