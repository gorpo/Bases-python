from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
"""este script é uma base de automatização em python para login  usando o selenium, 
é necessario que o drive esteja junto com o arquivo para que o navegador abra e nao existam erros
pode ser trocado o navegador a ser aberto na variavel self.driver e em webdriver é setado seu navegador,
lembre sempre de usar o drive pertinente ao seu navegador junto com arquivo.
OBS: este script apenas faz login , porem ali temos claramente como por um dado 
em uma entry e como acessar um botao e um link, isto basta para voce poder comentar e dar likes automaticamente,
bem como executar outras coisas na rede, mais coisas voce pode criar aprendendo usar o selenium.
ATENÇAO: para pegar as input ou dados de botao dentre outros basta ---INSPECIONAR O ELEMENTO---- em seu navegador e pegar uma id unica la
repare que a id sera formatada, irei dar um exemplo a seguir:

--- no site temos no elemento inspecionado name = 'email':

formatado para usar neste script ficaria:

"//input[@name = 'email']"
como podemos ver na linha 32 (variavel input-login)
"""
class facebookBot:
    def __init__(self,username,password):
        self.usuario = username
        self.senha = password
        self.driver = webdriver.Firefox()
        #// vamos pegar as informaçoes que sejam unicas em user e senha, inspecionando elemento no navegador
    def login(self):
        driver = self.driver
        driver.get('https://www.facebook.com/')
        time.sleep(2)

        input_login = driver.find_element_by_xpath("//input[@name = 'email']")
        input_login.clear()  #apaga caso tenha algo la
        input_login.send_keys(self.usuario)

        input_senha = driver.find_element_by_xpath("//input[@name = 'pass']")
        input_senha.clear()
        input_senha.send_keys(self.senha)

        #vamos simular o botao enter do teclado com o comando
        input_senha.send_keys(Keys.RETURN)

gorpo = facebookBot('seu email do facebook','sua senha do facebook')
gorpo.login()


