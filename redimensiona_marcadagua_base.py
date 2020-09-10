from PIL import Image
import os, sys




imagem = 'teste.jpg'


#imagem de entrada e marca dagua
imagem_entrada = Image.open(imagem)
watermark = Image.open('watermark.png')
# redimensiona imagem de entrada para 250px
imagem_entrada = imagem_entrada.resize((250, 250), Image.ANTIALIAS)
#pega as medidas da imagem de entrada
width, height = imagem_entrada.size
#cria uma imagem temporaria na memoria |  para transparent usar "RGBA" e (0,0,0,0)
imagem_final = Image.new('RGB', (width, height), (0, 0, 0))
#mescla as imagens de entrada e marca dagua na imagem da memoria
imagem_final.paste(imagem_entrada, (0, 0))
imagem_final.paste(watermark, (0, 0), mask=watermark)
#exibe a imagem
imagem_final.show()
#salva a imagem
imagem_final.save('sla.jpg')


