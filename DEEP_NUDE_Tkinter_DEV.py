# coding=utf-8
import cv2
import os
import sys
import subprocess
from run import process
import argparse
from tkinter import *




def main(inputpath, outpath):
	outputpath = 'b.jpg'
	if isinstance(inputpath, list):
		for item in inputpath:
			watermark = deep_nude_process(item)
			cv2.imwrite("output_"+item, watermark)
	else:
		watermark = deep_nude_process(inputpath)
		cv2.imwrite(outputpath, watermark)

def deep_nude_process(item):
    print('Processing {}'.format(item))
    dress = cv2.imread(item)
    h = dress.shape[0]
    w = dress.shape[1]
    dress = cv2.resize(dress, (512,512), interpolation=cv2.INTER_CUBIC)
    watermark = process(dress)
    watermark = cv2.resize(watermark, (w,h), interpolation=cv2.INTER_CUBIC)
    return watermark



if __name__ == '__main__':

	def clique():
		inputpath = 'a.jpg'
		outputpath = 'b.jpg'
		main(inputpath, outputpath)


	window = Tk()
	window.geometry("300x200+200+100")
	window.title("Manicomio Testes")
	mensagem = Label(window, text="Clique no botao", font="impact 20 bold")
	mensagem.pack()
	botao = Button(window, text="Clique Aqui", command= clique)
	botao.pack()
	window.mainloop()






