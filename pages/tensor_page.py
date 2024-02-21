from pages.base_page import BasePage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# tensor.ru
class TensorPage(BasePage):
    def get_block(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[p[contains(text(), 'Сила в людях')]]"))
        )

    def go_to_about(self, block):
        button = block.find_element(By.LINK_TEXT, "Подробнее")
        self.driver.execute_script("arguments[0].click();", button)


