from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.create_page import CreatePage
from pages.eco_friendly_page import EcoFriendlyPage
from pages.sale_page import SalePage
import pytest


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture()
def create_page(driver):
    return CreatePage(driver)


@pytest.fixture()
def eco_friendly_page(driver):
    return EcoFriendlyPage(driver)


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)
