from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


def start_driver() -> WebDriver:
    """
    start the driver for Firefox and open the correct Page
    """
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.implicitly_wait(30)
    driver.maximize_window()
    driver.get("http://127.0.0.1:8000/")
    driver.implicitly_wait(30)
    return driver


def quit_driver(driver: WebDriver) -> None:
    driver.quit()
