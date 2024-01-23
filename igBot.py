from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

class InstagramBot:
    def __init__(self, username, password):
        # Inicialização da classe InstagramBot com nome de usuário e senha
        self.username = username
        self.password = password
        # Configuração do perfil do Firefox para aceitar idiomas em português e desativar notificações
        firefoxProfile = webdriver.FirefoxProfile()
        firefoxProfile.set_preference("intl.accept_languages", "pt,pt-BR")
        firefoxProfile.set_preference("dom.webnotifications.enabled", False)
        # Inicialização do driver do Firefox com o perfil configurado
        self.driver = webdriver.Firefox(
            firefox_profile=firefoxProfile, executable_path=r"C:\Users\wilia\Desktop\geckodriver-v0.33.0-win64\geckodriver.exe")

    def login(self):
        # Método para realizar o login no Instagram
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(3)
        # Encontrar e preencher o campo de usuário
        user_element = driver.find_element_by_xpath(
            "//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        time.sleep(3)
        # Encontrar e preencher o campo de senha
        password_element = driver.find_element_by_xpath(
            "//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        time.sleep(3)
        # Pressionar Enter para fazer login
        password_element.send_keys(Keys.RETURN)
        time.sleep(5)
        # Chamar o método para comentar nas fotos com uma hashtag específica
        self.comente_nas_fotos_com_a_hashtag(
            "culinaria"
        )  # Altere aqui para a hashtag que você deseja usar.

    @staticmethod
    def type_like_a_person(sentence, single_input_field):
        """ Simula a digitação como uma pessoa """
        # Método para simular a digitação como uma pessoa
        print("Iniciando a digitação na área de compartilhamento de mensagens")
        for letter in sentence:
            single_input_field.send_keys(letter)
            time.sleep(random.randint(5, 10) / 30)

    def comente_nas_fotos_com_a_hashtag(self, hashtag):
        # Método para comentar nas fotos com uma hashtag específica
        links_de_posts = []
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(5)
        for i in range(1, 6):  # Altere o segundo valor para a quantidade de páginas desejada
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
        # Encontrar todos os links das fotos com a hashtag
        hrefs = driver.find_elements_by_tag_name("a")
        pic_hrefs = [elem.get_attribute("href") for elem in hrefs]
        print(hashtag + " fotos: " + str(len(pic_hrefs)))
        for link in pic_hrefs:
            try:
                # Adicionar links de postagens à lista
                if link.index("/p/") != -1:
                    links_de_posts.append(link)
            except ValueError:
                pass

        # Iterar sobre as postagens e adicionar comentários
        for pic_href in links_de_posts:
            driver.get(pic_href)
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            try:
                # Comentários para adicionar às postagens
                comments = [
                    "teste 91😘😘",
                    "teste12323213🙂🙂",
                    "dawindonawd😉😉",
                    "dawdawdscaswa😊",
                ]
                # Aguardar até que o campo de comentário esteja presente
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "_akhn"))).click()
                comment_input_box = driver.find_element_by_class_name("_akhn")
                time.sleep(random.randint(9, 10))
                # Chamar o método para simular a digitação do comentário
                self.type_like_a_person(
                    random.choice(comments), comment_input_box)
                time.sleep(random.randint(15, 20))
                # Clicar no botão "Publicar" para enviar o comentário
                driver.find_element_by_xpath(
                    "//button[contains(text(), 'Publicar')]"
                ).click()
                time.sleep(random.randint(3, 5))
            except Exception as e:
                print(e)
                time.sleep(5)

    def __del__(self):
        # Método para encerrar o driver do navegador quando a instância é destruída
        self.driver.quit()

# Instanciar a classe InstagramBot e fazer login
cacadordebitch = InstagramBot(
    "shaulinpork", "shaulinmatadordeporco"
)  # Substitua com seu usuário e senha
cacadordebitch.login()
