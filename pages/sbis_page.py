import time

from pages.base_page import BasePage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# sbis.ru
class SBISPage(BasePage):
    def go_to_contacts(self):
        contacts_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Контакты")))
        contacts_link.click()

    def go_to_download(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Скачать локальные версии")))
        self.driver.execute_script("arguments[0].click();", button)
        time.sleep(60)
