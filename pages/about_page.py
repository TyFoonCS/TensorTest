from pages.base_page import BasePage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# tensor.ru/about
class AboutPage(BasePage):
    def is_about_tensor_page_opened(self):
        url = self.driver.current_url
        return url == "https://tensor.ru/about"

    def are_images_dimensions_equal(self):
        block = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[div[h2[contains(text(), 'Работаем')]]]"))
        )
        inner_block = block.find_element(By.XPATH, "./div[2]")
        images = inner_block.find_elements(By.TAG_NAME, "img")

        first_image_dimensions = images[0].size
        for image in images[1:]:
            if image.size != first_image_dimensions:
                return False
        return True
