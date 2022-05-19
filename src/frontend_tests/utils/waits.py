from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.common.exceptions import *

def document_ready(driver: WebDriver) -> bool:
    """
    checks if the page is fully loaded, using the ready state
    """
    return driver.execute_script('return document.readyState') == 'complete'

def wait_for_page_to_load(driver: WebDriver, timeout:int = 10, poll_frequency:int = 1) -> None:
    wait = WebDriverWait(driver, timeout, poll_frequency, ignored_exceptions=[StaleElementReferenceException, NoSuchElementException])
    wait.until(document_ready)
