from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        firefoxProfile = webdriver.FirefoxProfile()
        firefoxProfile.set_preference("intl.accept_languages", "pt,pt-BR")
        firefoxProfile.set_preference("dom.webnotifications.enabled", False)
        self.driver = webdriver.Firefox(
            firefox_profile=firefoxProfile, executable_path=r"C:\Users\wilia\Desktop\geckodriver-v0.33.0-win64\geckodriver.exe")

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(3)
        user_element = driver.find_element_by_xpath(
            "//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        time.sleep(3)
        password_element = driver.find_element_by_xpath(
            "//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        time.sleep(3)
        password_element.send_keys(Keys.RETURN)
        time.sleep(5)
        self.comente_nas_fotos_com_a_hashtag(
            "culinaria"
        )  # Altere aqui para a hashtag que você deseja usar.

    @staticmethod
    def type_like_a_person(sentence, single_input_field):
        """ Este código irá basicamente permitir que você simule a digitação como uma pessoa """
        print("going to start typing message into message share text area")
        for letter in sentence:
            single_input_field.send_keys(letter)
            time.sleep(random.randint(5, 10) / 30)

    def comente_nas_fotos_com_a_hashtag(self, hashtag):
        links_de_posts = []
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(5)
        for i in range(1, 6):  # Altere o segundo valor para a quantidade de páginas desejada
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
        hrefs = driver.find_elements_by_tag_name("a")
        pic_hrefs = [elem.get_attribute("href") for elem in hrefs]
        print(hashtag + " fotos: " + str(len(pic_hrefs)))
        for link in pic_hrefs:
            try:
                if link.index("/p/") != -1:
                    links_de_posts.append(link)
            except ValueError:
                pass

        for pic_href in links_de_posts:
            driver.get(pic_href)
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            try:
                comments = [
                    "UaU amiga, realmente está demais mas vc já visitou nossa bio? descubra como emagrecer passando em nosso perfil!!!😘😘",
                    "Olha que foto massa!, mas será que você está satisfeita com seu corpo?? descubra como ter o corpo ideal em nosso perfil!!🙂🙂",
                    "Olha, você parece estar realmente bem, mas entre em meu perfil e encontre a dieta ideal para o seu corpo!!😉😉",
                    "Você deve entrar em meu perfil para ter a dieta ideal e possuir um corpinho ótimo e gato 😊",
                ]  # Remova esses comentários e insira os seus comentários aqui
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "Ypffh"))).click()
                comment_input_box = driver.find_element_by_class_name("Ypffh")
                time.sleep(random.randint(2, 10))
                self.type_like_a_person(
                    random.choice(comments), comment_input_box)
                time.sleep(random.randint(3, 10))
                driver.find_element_by_xpath(
                    "//button[contains(text(), 'Publicar')]"
                ).click()
                time.sleep(random.randint(3, 5))
            except Exception as e:
                print(e)
                time.sleep(5)

    def __del__(self):
        self.driver.quit()


cacadordebitch = InstagramBot(
    "shaulinpork", "shaulinmatadordeporco"
)  # Entre com o usuário e senha aqui
cacadordebitch.login()
