from tkinter import *

def aoClicar():
    mensagem["text"]="O Botão Foi Clicado"



window = Tk()
window.geometry("300x200+200+100")

window.title("Manicomio Testes")
mensagem = Label(window, text="Clique no botao", font="impact 20 bold")
mensagem.pack()
botao = Button(window, text="Clique Aqui", command=aoClicar)
botao.pack()
window.mainloop()


