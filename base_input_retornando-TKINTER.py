from tkinter import*
janela = Tk()
janela.geometry('605x605')
janela.title("Manicomio Testes")

#background
logo = PhotoImage(file='bg.png')
label_logo = Label (janela, image=logo)
label_logo.place(x=1,y=1)

#enviar texto
def texto():
    inputValue=caixa_texto.get("1.0", "end-1c")
    mensagem["text"] = str("Comando enviado, seu comando foi {}".format(inputValue))
    if inputValue == 'asd':
        print(inputValue)


caixa_texto=Text(janela, height=1, width=30)
caixa_texto.pack(side=TOP)
caixa_texto.place(x=50, y=120)


botao=Button(janela, height=1, width=10, text="Enviar",command=lambda: texto())
botao.pack(side=TOP)
botao.place(x=310,y=118)


mensagem = Label(janela,)
mensagem.pack()
mensagem.place(x=50,y=150)
mensagem_inserida = caixa_texto.get("1.0", "end-1c")
mensagem["text"] = str("Aguarde:{}".format(mensagem_inserida))
print(mensagem_inserida)











janela.mainloop()                      #A Janela para ser aberta precisa de um loop, então chamamos:



