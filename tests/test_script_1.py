import pytest

from selenium import webdriver
from pages.sbis_page import SBISPage
from pages.contacts_page import ContactsPage
from pages.tensor_page import TensorPage
from pages.about_page import AboutPage


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_script_1(browser):
    # Инициализация страниц
    sbis_page = SBISPage(browser)
    contacts_page = ContactsPage(browser)
    tensor_page = TensorPage(browser)
    about_page = AboutPage(browser)

    # Шаги сценария
    sbis_page.open("https://sbis.ru/")

    # Переход в контакты
    sbis_page.go_to_contacts()

    # Переход по баннеру на tensor.ru
    contacts_page.click_tensor_banner()

    # Переключение на новую вкладку
    browser.switch_to.window(browser.window_handles[1])

    # Проверки на странице tensor.ru
    block = tensor_page.get_block()
    assert block.is_displayed()
    tensor_page.go_to_about(block)

    # Проверки на странице tensor.ru/about
    assert about_page.is_about_tensor_page_opened()
    assert about_page.are_images_dimensions_equal()
