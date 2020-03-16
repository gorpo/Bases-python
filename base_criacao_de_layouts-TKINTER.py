# Primeiramente importamos o tkinter, logo apos isto criamos uma variavel com o nome "janela" para chamar o tkinter dentro de nosso script
# de pois definimos o tamanho da "janela" com o comando geometry() o qual podemos inserir o tamanho da janela.
#No segundo bloco temos o exemplo de como chamar uma imagem, e logo apos de como chamar textos e botoes, pode reparar que tudo é sua_string.comandos do tkinter
#Comando Label() é sempre usado para definir oque vai aparecer ali na janela, tudo q vai apareceer e ja foi identado vai ser chamado ali dentro.
# comando place = posiciona em algum lugar da tela Button() gera um botao
# vemos no botao o comando botao.grid(row=0, column=1) onde row= e a linha e column a coluna que queremos que ele fique.


from tkinter import*
janela = Tk()                                #aqui ela diz que vai ser uma janela de tkinter,
janela.geometry('605x605')                   #define o tamanho da janela

logo = PhotoImage(file='bg.png')           #como chamar uma imagem dentro do tkinter
label_logo = Label (janela, image=logo)         #cria a Label para por a imagem na janela, tudo q vamos por ja janela tem q ser identado como Label, porem so aparece se chamaar ela com o comando abaixo
label_logo.place(x=1,y=1)                       #identa a posição da imagem em dois eixos XY

frame1 = Frame(janela)                       #Inicia um frame na nossa janela, temos que cria um frame para cada........
frame1.pack(side=TOP)                        #indica onde este frame ira ficar na nossa janela
texto1 = Label(frame1, text='Soma')           #Label() cria textl
texto1.grid(row=0, column=0)                  #row é a tabela e comlun a posiçao da coluna na tabela
botao1 = Button(frame1,text='=')             #Button() cria botao
botao1.grid(row=0, column=1)                 #row=0 é uma tabela ja o column seleciona a posiçao na tabela
frame1.place(x=50,y=120)                    #identa a posição do bloco aqui no caso do frame1
#exemplo de uma imagem na Label
frame2 = Frame(janela)
frame2.pack(side=TOP)
img2 = PhotoImage(file='label.png')
label2 = Label(frame2, image=img2)
label2.grid(row=0, column=0)
frame2.place(x=150,y=120)
#exemplo de uma imagem no botao
frame3 = Frame(janela)
frame3.pack(side=TOP)
img3 = PhotoImage(file='btn.png')
botao2 = Button(frame3, image=img3)
botao2.grid(row=0, column=0)
frame3.place(x=340, y=120)


janela.mainloop()                      #A Janela para ser aberta precisa de um loop, então chamamos:



