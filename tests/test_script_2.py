import pytest

from selenium import webdriver
from pages.sbis_page import SBISPage
from pages.contacts_page import ContactsPage


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_script_2(browser):
    # Инициализация страниц
    sbis_page = SBISPage(browser)
    contacts_page = ContactsPage(browser)

    # Шаги сценария
    sbis_page.open("https://sbis.ru/")

    # Переход в контакты
    sbis_page.go_to_contacts()

    # Проверки информации о регионе и ее изменения
    assert contacts_page.check_region("Республика Татарстан")
    contacts_page.change_region()
    assert contacts_page.check_region_changed()
