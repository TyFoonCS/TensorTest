import time

from pages.base_page import BasePage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# sbis.ru
class DownloadPage(BasePage):
    def go_to_contacts(self):
        contacts_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Контакты")))
        contacts_link.click()

    def go_to_download(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Скачать локальные версии")))
        self.driver.execute_script("arguments[0].click();", button)

    def download_plugin(self, download_path):
        plugin_block = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-id='plugin']"))
        )
        plugin_block.click()
        download_link = self.driver.find_element(
            By.CSS_SELECTOR, "a[href='https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe']")
        download_link.click()
        time.sleep(60)
        options = self.driver.ChromeOptions()
        prefs = {"download.default_directory": download_path}
        options.add_experimental_option("prefs", prefs)
