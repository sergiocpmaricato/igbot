from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


#Variaveis de acesso ao instagram
seuusuario = 'DIGITE SEU USUARIO AQUI'
suasenha = 'DIGITE SUA SENHA AQUI'
pagina = 'DIGITE A PAGINA DO INSTAGRAMQUE DESEJA COMENTAR (INCLUINDO O HTTP)' # Coloque aqui a pagina que deseja comentar!"

contador = 1

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(
            executable_path=r"./geckodriver.exe")

    def login(self):
        driver = self.driver
        driver.get(pagina) 
        time.sleep(5)
        try:
            login_button = driver.find_element_by_xpath(
                    "//button[@class='sqdOP  L3NKy   y3zKF     ']"
                )
            login_button.click()
            time.sleep(3)
            user_element = driver.find_element_by_xpath("//input[@name='username']")
            user_element.clear()
            user_element.send_keys(self.username)
            print('Efetuando login.')
            print('')
            password_element = driver.find_element_by_xpath("//input[@name='password']")
            password_element.clear()
            password_element.send_keys(self.password)
            time.sleep(5)
            password_element.send_keys(Keys.RETURN)
            time.sleep(5)
            nao_agora = driver.find_element_by_xpath("//button[@class='sqdOP yWX7d    y3zKF     ']")
            nao_agora.click()
            try:
                notificacao = driver.find_element_by_xpath("//button[@class='aOOlW   HoLwm ']")
                notificacao.click()
            except:
                pass
            print('Logado com sucesso.')
            print('')
        except:
            print('O Usuario ja fez login!')
            ('')
    @staticmethod
    def digite_como_uma_pessoa(self, user, onde_digitar):
        for letra in user:
            onde_digitar.send_keys(letra)
            time.sleep(random.randint(1,5)) # Variação de tempo entre uma letra e outra.

    def comentar(self):
        arquivo_usuarios = open("usuarios.txt", 'r')
        lista_de_usuarios = [line for line in arquivo_usuarios]
        usuario_aleatorio = str(random.choice(lista_de_usuarios))
        print('Escolhendo um usuário aleatoriamente.')
        print('')
        print(f'Usuário {usuario_aleatorio} foi selecionado.')
        print('')
        driver = self.driver
        campo_comentario = driver.find_element_by_class_name('Ypffh')
        campo_comentario.click()
        campo_comentario = driver.find_element_by_class_name('Ypffh')
        time.sleep(random.randint(5, 10)) #Defina aqui, a variação de tempo em cada comentario.
        print(f'Este é o comentario de Nº{contador}')
        print(f'Marcando o usuário {usuario_aleatorio}')
        print('')
        self.digite_como_uma_pessoa(self, usuario_aleatorio, campo_comentario)
        tempo_de_espera = random.randint(30, 120)
        print(f'Sistema AntBan: Aguardando {tempo_de_espera} segundos até publicar.')
        print('')
        time.sleep(tempo_de_espera)
        publicar = driver.find_element_by_xpath("//button[@class='sqdOP yWX7d    y3zKF     ']")
        publicar.send_keys(Keys.ENTER)
        publicar.click()
        time.sleep(10) # Tempo de publicação
        driver.refresh()
        time.sleep(7)
        print('Recarregando a pagina.')
        print('')


igbot = InstagramBot(seuusuario, suasenha)
igbot.login()
while True:
    igbot.comentar()
    contador += 1
