from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

"""este script faz login no instagram e de acordo com a tag ele da like nos posts, podem ser acrescidas funçoes nele pois 
analisando o script esta claro onde temos exemplos de como pegar dados de uma entry, de um botao, de um botao de like, etc..
este script é uma base de automatização em python para login  usando o selenium, 
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
class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox() 

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(3)
        #acha a entrada de dados USUARIO e insere dados nela
        user_element = driver.find_element_by_xpath("//input[@name='username']")  #procura o elemento de acordo com a id name
        user_element.clear()                      #limpa o campo de entrada de login de usuario caso tenha algum dado
        time.sleep(random.randint(4, 6))           #cria um sleep para dar tempo de limpar e carregar a pagina
        user_element.send_keys(self.username)   #sendkeys envia os dados para serem digitados automaticamente
        time.sleep(random.randint(4, 6))
        #acha a entrade de por senhas e insere dados nela, mesmos comentarios de USUARIO acima servem aqui
        password_element = driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        time.sleep(random.randint(4, 6))
        password_element.send_keys(Keys.RETURN)  #aqui ele simula o enter do teclado (legal ne? aprenda mais sobre esta lib)
        time.sleep(random.randint(4, 6))
        self.curtir_fotos_com_a_hastag("programação")  # Altere aqui para a hashtag que você deseja usar.

    @staticmethod
    def type_like_a_person(sentence, single_input_field):
        """ Este código irá basicamente permitir que você simule a digitação como uma pessoa """
        print("going to start typing message into message share text area")
        for letter in sentence:
            single_input_field.send_keys(letter)
            time.sleep(random.randint(1, 5) / 30)

    def curtir_fotos_com_a_hastag(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(5)
        for i in range(
            1, 3
        ):  # Altere o segundo valor aqui para que ele desça a quantidade de páginas que você quiser: quer que ele desça 5 páginas então você deve alterar de range(1,3) para range(1,5)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
        hrefs = driver.find_elements_by_tag_name("a")
        pic_hrefs = [elem.get_attribute("href") for elem in hrefs]
        print(hashtag + " fotos: " + str(len(pic_hrefs)))
        testes = [
            href
            for href in pic_hrefs
            if hashtag in href and href.index("https://www.instagram.com/p") != -1
        ]

        for pic_href in pic_hrefs:
            try:
                pic_href.index("https://www.instagram.com/p")
            except ValueError as err:
                print("pulando link inválido")
                continue
            driver.get(pic_href)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                driver.find_element_by_xpath('//button[@class="dCJp8 afkep"]').click()
                time.sleep(random.randint(19, 23))
            except Exception as e:
                print(e)
                time.sleep(5)


gorpoBot = InstagramBot('seu usuario do instagram','sua senha do instagram')  # Entre com o usuário e senha aqui
gorpoBot.login()