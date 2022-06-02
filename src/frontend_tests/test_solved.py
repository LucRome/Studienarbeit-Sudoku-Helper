import unittest as ut
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from typing import List

from .utils.waits import wait_for_page_to_load

from .utils.web_driver_utils import start_driver, quit_driver
from .utils.input_utils import enter_sudoku, submit_sudoku, write_value_in_field, clear_all_fields
from backend.sudoku.base import ALL_FIELD_VALUES, FIELD_VALUE_MAX, FIELD_VALUE_MIN, NINE_RANGE
from .utils.modal_tests import test_modals

class TestIndex(ut.TestCase):
    """
    the Tests for the index Page
    """
    driver: WebDriver = None

    def setUp(self) -> None:
        self.driver = start_driver()

    def tearDown(self) -> None:
        quit_driver(self.driver)
        self.driver = None

    def test_solved_page(self):
        """
        test the input fields of the sudoku on whether they accept the inputs correctly
        """
        values = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [4, 5, 6, 7, 8, 9, 1, 2, 3],
            [7, 8, 9, 1, 2, 3, 4, 5, 6],
            [2, 3, 4, 5, 6, 7, 8, 9, 1],
            [5, 6, 7, 8, 9, 1, 2, 3, 4],
            [8, 9, 1, 2, 3, 4, 5, 6, 7],
            [3, 4, 5, 6, 7, 8, 9, 1, 2],
            [6, 7, 8, 9, 1, 2, 3, 4, 5],
            [9, 1, 2, 3, 4, 5, 6, 7, 8]
        ]

        enter_sudoku(self.driver, values)
        submit_sudoku(self.driver)

        # skip verified page
        self.driver.find_element(by=By.ID, value='solve-sudoku-btn')
        wait_for_page_to_load(self.driver, timeout=120)

        # tests
        # success message visible
        self.assertTrue(self.driver.find_element(by=By.CLASS_NAME, value='alert-success').is_displayed())