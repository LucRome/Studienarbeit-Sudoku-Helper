import unittest as ut
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException
from typing import List

from .utils.web_driver_utils import start_driver, quit_driver
from .utils.input_utils import write_value_in_field, clear_all_fields, enter_sudoku, submit_sudoku
from backend.sudoku.base import ALL_FIELD_VALUES, FIELD_VALUE_MAX, FIELD_VALUE_MIN, NINE_RANGE
from backend.dev_tools.algorithm_sudokus import GRID12
from .utils.modal_tests import test_modals

SUDOKU_VALID = GRID12
SUDOKU_INVALID = [
    [None, 2, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, 2, None, None, None, None],
    [None, 4, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, 8, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, 9, None, None, None, None, None, None],
    [None, None, None, None, None, 6, None, None, None],
    [None, None, None, None, None, None, None, None, None],
]

class TestVerified(ut.TestCase):
    """
    Tests for the Page that displays whether the submitted Sudoku is correct
    """
    driver: WebDriver = None

    def setUp(self) -> None:
        self.driver = start_driver()

    def tearDown(self) -> None:
        quit_driver(self.driver)
        self.driver = None

    def test_valid(self):
        """
        test when a valid sudoku is entered
        """
        enter_sudoku(self.driver, SUDOKU_VALID)
        submit_sudoku(self.driver)
        
        # Success message
        success_msg = self.driver.find_element(by=By.CSS_SELECTOR, value='div.alert-success')
        self.assertTrue(success_msg.is_displayed())
        success_msg.find_element(by=By.CSS_SELECTOR, value='button[data-bs-dismiss="alert"]').click()
        # (alerts are completely removed from the DOM, when closed)
        self.assertRaises(StaleElementReferenceException, success_msg.is_displayed)

        # Inputs are readonly
        inputs = self.driver.find_elements(by=By.CSS_SELECTOR, value='input[type="number"]')
        for input in inputs:
            self.assertEqual(input.get_attribute('readonly'), 'true')
        
        # candidates
        candidates = self.driver.find_elements(by=By.CLASS_NAME, value='candidate-table')
        self.assertGreater(len(candidates), 0)
        for can in candidates:
            self.assertFalse(can.is_displayed())
        self.driver.find_element(by=By.ID, value='toggle-candidates-btn').click()
        for can in candidates:
            self.assertTrue(can.is_displayed())
        self.driver.find_element(by=By.ID, value='toggle-candidates-btn').click()
        for can in candidates:
            self.assertFalse(can.is_displayed())

        test_modals(self, self.driver, quickinfo=True, help=True)
    
    def test_invalid(self):
        """
        test when a invalid sudoku is entered
        """
        enter_sudoku(self.driver, SUDOKU_INVALID)
        submit_sudoku(self.driver)

        # error message
        error_msg = self.driver.find_element(by=By.CSS_SELECTOR, value='div.alert-danger')
        self.assertTrue(error_msg.is_displayed())
        error_msg.find_element(by=By.CSS_SELECTOR, value='button[data-bs-dismiss="alert"]').click()
        # (alerts are completely removed from the DOM, when closed)
        self.assertRaises(StaleElementReferenceException, error_msg.is_displayed)

        # inputs are not readonly
        inputs = self.driver.find_elements(by=By.CSS_SELECTOR, value='input[type="number"]')
        for input in inputs:
            self.assertEqual(input.get_attribute('readonly'), None)

        # validate button is present
        self.assertTrue(self.driver.find_element(by=By.ID, value='submit-sudoku-btn').is_enabled())

        # modals
        test_modals(self, self.driver, quickinfo=True, help=True)
