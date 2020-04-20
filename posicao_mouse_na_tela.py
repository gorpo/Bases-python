from tkinter import *
from pyautogui import position
from time import sleep
janela = Tk()
largura = janela.winfo_screenwidth()   #mede a largura do monitor
altura = janela.winfo_screenheight()   #mede a altura do monitor
texto = Text(janela, font=("arial", 8), borderwidth=1)  #configuracoes do texto apresentado
janela.wm_attributes('-topmost', 'true')   #verificar comentarios entre aspas abaixo
"""Atributos do Windows
A maioria das opções assume um valor verdadeiro / falso
-alpha double
     quão opaca é a janela geral; observe que alterar entre 1,0 e qualquer outro valor pode fazer com que a janela pisque (Tk altera a classe de janela usada para implementar o nível superior).
-fullscreen boolean
     controla se a janela preenche a tela inteira, incluindo a barra de tarefas
- disabled boolean
     torna impossível interagir com a janela e redesenha o foco
-toolwindow boolean
     cria uma janela com um único botão fechar (que é menor que o normal) à direita da barra de título
-topmost boolean
     garante que a janela fique sempre em cima de todas as outras janelas"""

while True:
    x, y = position()                   #reconhece a posição de x e y
    posicaoX = str(x).rjust(4)          #ajusta o texto do lado da posicao X na GUI
    posicaoY = str(y).rjust(4)          #ajusta o texto do lado da posicao Y na GUI
    posicao_mouse = 'X: ' + posicaoX + ' Y: ' + posicaoY    #cria o texto final apresentado na GUI (melhorar isto ta uma bosta)
    texto.insert(INSERT, posicao_mouse)    #insere o texto na GUI
    texto.pack()                           #Empacota a GUI
    sleep(0.0005)                          #descansinho para atulializaçao da GUI
    x = int(posicaoX)     #transforma o valor da posiçaoX como inteiro
    y = int(posicaoY)      #transforma o valor da posiçaoX como inteiro
    janela.wm_overrideredirect(1)  #este maravilhoso comando esconde o padrao do tkinter, basta mudar ali entre 0 e 1

    w = 79      #largura para janela
    h = 17      #altura para janela
    janela.geometry(f'{w}x{h}+{x - (w + 1 + 10)}+{ (y - (h + 30 + 10))}')
    """SEGREDO DA GAMBIARRA PARA MANTER A CAIXA DE TEXTO LONGE DO MOUSE SEGUINDO ELE>
        primeira parte - {w}x{h} - Pega o valor de w e h para fazer a dimensao da janela tkinter
       Ai para fixar a posiçao fixa fiz aqueles calculos ate chegar em uma posiçao que a caixa siga o mouse mas
       nao atrapalhe a visao e o click, se removido os valores como exemplo a baixo a caixa do tkinter
       irá ficar  no canto superior da tela, ou pode ajudar da melhor forma que quiser
       --->> Exemplo sem seguir mouse:      janela.geometry(f'{w}x{h}')"""
    janela.update()        #atualiza a janela com o texto
    texto.delete(1.0, END) #deleta o valor para sempre que passar no loop do while ele atualize o texto
    texto.pack()           #empacota o texto
