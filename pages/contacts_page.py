import time

from pages.base_page import BasePage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# sbis.ru/contacts/
class ContactsPage(BasePage):
    def click_tensor_banner(self):
        tensor_banner = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//a[contains(@href, 'tensor.ru') and not(contains(@href, 'tensor.ru/about'))]")))
        tensor_banner.click()

    def check_region(self, correct_region):
        region = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "sbis_ru-Region-Chooser__text"))).text
        return region == correct_region

    def change_region(self):
        region_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "sbis_ru-Region-Chooser"))
        )
        region_element.click()

        change_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "span[title='Камчатский край']"))
        )
        change_button.click()
        time.sleep(5)

    def check_region_changed(self):
        city = self.driver.find_element(By.CLASS_NAME, "sbisru-Contacts-List__city").text
        if city == "Петропавловск-Камчатский" and \
                self.check_region("Камчатский край") and \
                "kamchatskij-kraj" in self.driver.current_url and \
                "Камчатский край" in self.driver.title:
            return True
        else:
            return False


