from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from typing import Optional

from .waits import wait_for_page_to_load

WAIT_TIME = 20


class DriverGetter:
    driver = None

    @staticmethod
    def get_driver() -> WebDriver:
        if DriverGetter.driver is None:
            DriverGetter.driver =  webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        return DriverGetter.driver

def start_driver(page: str = '') -> WebDriver:
    """
    start the driver for Firefox and open the correct Page
    """
    driver = DriverGetter.get_driver()
    # driver.maximize_window()
    driver.get(f'http://127.0.0.1:8000/{page}')

    # use smartphone dimensions
    driver.set_window_size(360, 800)

    driver.implicitly_wait(WAIT_TIME)
    wait_for_page_to_load(driver)

    return driver


def quit_driver(driver: WebDriver) -> None:
    # driver.quit()
    pass
