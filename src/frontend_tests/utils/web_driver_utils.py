from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from .waits import wait_for_page_to_load


def start_driver(page: str = '') -> WebDriver:
    """
    start the driver for Firefox and open the correct Page
    """
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    # driver.maximize_window()
    driver.get(f'http://127.0.0.1:8000/{page}')
    # driver.implicitly_wait(60)
    wait_for_page_to_load(driver)
    return driver


def quit_driver(driver: WebDriver) -> None:
    driver.quit()
