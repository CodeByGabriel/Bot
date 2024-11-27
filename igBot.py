# Importa a classe 'webdriver' do módulo 'selenium'.
from selenium import webdriver
# Importa a classe 'Keys' do módulo 'selenium.webdriver.common.keys'.
from selenium.webdriver.common.keys import Keys
# Importa a classe 'By' do módulo 'selenium.webdriver.common.by'.
from selenium.webdriver.common.by import By
# Importa a classe 'WebDriverWait' do módulo 'selenium.webdriver.support.ui'.
from selenium.webdriver.support.ui import WebDriverWait
# Importa o módulo 'expected_conditions' do pacote 'selenium.webdriver.support' e o renomeia como 'EC'.
from selenium.webdriver.support import expected_conditions as EC
# Importa a classe 'Service' para inicializar o driver com caminho personalizado.
from selenium.webdriver.firefox.service import Service
# Importa a classe 'Options' para configurar o navegador Firefox.
from selenium.webdriver.firefox.options import Options
# Importa o módulo 'time', que fornece funções relacionadas ao tempo.
import time
# Importa o módulo 'random', que fornece funções para gerar números pseudoaleatórios.
import random

class InstagramBot:
    def __init__(self, username, password):
        # Inicialização da classe InstagramBot com nome de usuário e senha.
        self.username = username
        self.password = password
        
        # Substituição da configuração do perfil pelo uso da classe Options.
        options = Options()
        # Configuração para aceitar o idioma português e desativar notificações.
        options.set_preference("intl.accept_languages", "pt,pt-BR")
        options.set_preference("dom.webnotifications.enabled", False)

        # Substituição de 'firefox_profile' por 'options' e uso da classe Service.
        service = Service(r"C:\Users\teste\Desktop\geckodriver\geckodriver.exe")
        self.driver = webdriver.Firefox(service=service, options=options)

    def login(self):
        # Método para realizar o login no Instagram.
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(3)
        
        # Encontrar e preencher o campo de usuário.
        user_element = driver.find_element(By.XPATH, "//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        time.sleep(3)
        
        # Encontrar e preencher o campo de senha.
        password_element = driver.find_element(By.XPATH, "//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        time.sleep(3)
        # Pressionar Enter para fazer login.
        password_element.send_keys(Keys.RETURN)
        time.sleep(5)
        
        # Chamar o método para comentar nas fotos com uma hashtag específica.
        self.comente_nas_fotos_com_a_hashtag("culinaria")  # Alterar aqui para a hashtag desejada.

    @staticmethod
    def type_like_a_person(sentence, single_input_field):
        """ Simula a digitação como uma pessoa """
        # Método para simular a digitação como uma pessoa.
        print("Iniciando a digitação na área de compartilhamento de mensagens")
        for letter in sentence:
            single_input_field.send_keys(letter)
            time.sleep(random.randint(5, 10) / 15)

    def comente_nas_fotos_com_a_hashtag(self, hashtag):
        # Método para comentar nas fotos com uma hashtag específica.
        links_de_posts = []
        driver = self.driver
        driver.get(f"https://www.instagram.com/explore/tags/{hashtag}/")
        time.sleep(5)
        
        for i in range(1, 6):  # Alterar o segundo valor para a quantidade de páginas desejada.
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
        
        # Uso da nova API 'find_elements' com 'By'.
        hrefs = driver.find_elements(By.TAG_NAME, "a")
        pic_hrefs = [elem.get_attribute("href") for elem in hrefs]
        print(f"{hashtag} fotos: {len(pic_hrefs)}")
        
        for link in pic_hrefs:
            try:
                if "/p/" in link:
                    links_de_posts.append(link)
            except ValueError:
                pass

        for pic_href in links_de_posts:
            driver.get(pic_href)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                # Comentários para adicionar às postagens.
                comments = ["teste 91", "teste12323213", "dawindonawd", "dawdawdscaswa"]
                
                # Atualização do uso de WebDriverWait com a nova API.
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "_akhn"))
                ).click()
                comment_input_box = driver.find_element(By.CLASS_NAME, "_akhn")
                time.sleep(random.randint(9, 10))
                self.type_like_a_person(random.choice(comments), comment_input_box)
                time.sleep(random.randint(15, 20))
                driver.find_element(By.XPATH, "//button[contains(text(), 'Publicar')]").click()
                time.sleep(random.randint(5, 8))
            except Exception as e:
                print(e)
                time.sleep(7)

    def __del__(self):
        # Método para encerrar o driver do navegador quando a instância é destruída.
        try:
            self.driver.quit()
        except AttributeError:
            pass

# Instanciar a classe InstagramBot e fazer login.
cacadordebitch = InstagramBot("username", "passasddawword")  # Substitua com seu usuário e senha.
cacadordebitch.login()
