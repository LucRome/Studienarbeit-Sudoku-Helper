from typing import List
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.types import AnyKey

from backend.sudoku.base import NINE_RANGE
from .waits import wait_for_page_to_load


def write_value_in_field(field: WebElement, value: AnyKey) -> None:
    """
    writes the given value into the given field (using clear + tab)
    """
    field.clear()
    field.send_keys(value)
    field.send_keys(Keys.TAB)

def clear_all_fields(driver: WebDriver) -> None:
    """
    Clears all fields of the sudoku
    """
    for row in NINE_RANGE:
        for col in NINE_RANGE:
            driver.find_element(by=By.ID, value=f'{row}_{col}').clear()

def enter_sudoku(driver: WebDriver, values: List[List[int]]) -> None:
    """
    Fills the sudoku Form with the given values
    """
    for row in NINE_RANGE:
        for col in NINE_RANGE:
            if values[row][col]:
                field = driver.find_element(by=By.ID, value=f'{row}_{col}')
                write_value_in_field(field, values[row][col])

def submit_sudoku(driver: WebDriver) -> None:
    """
    Submits the Sudoku
    """
    driver.find_element(by=By.ID, value='submit-sudoku-btn').click()
    wait_for_page_to_load(driver, timeout=120, poll_frequency=5)
    