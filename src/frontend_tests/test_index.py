import unittest as ut
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from typing import List

from .utils.web_driver_utils import WAIT_TIME, start_driver, quit_driver
from .utils.input_utils import write_value_in_field, clear_all_fields
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

    def test_inputs_simple(self):
        """
        test the input fields of the sudoku on whether they accept the inputs correctly
        """

        input = self.driver.find_element(by=By.ID, value='0_0')
        submit_btn = self.driver.find_element(by=By.ID, value='submit-sudoku-btn')

        self.assertTrue(input.is_displayed() and input.is_enabled())

        # correct values
        for value in ALL_FIELD_VALUES:
            write_value_in_field(input, value)
            # no error classes should occur
            self.assertEqual(input.get_attribute('class'), '')
            self.assertEqual(input.get_attribute('value'), str(value))
            self.assertTrue(submit_btn.is_enabled())

        # edge cases wrong
        for value in [FIELD_VALUE_MIN - 1, FIELD_VALUE_MAX + 1]:
            write_value_in_field(input, value)
            # error classes should occur, submit should be blocked
            self.assertIn(input.get_attribute('class'), 'sudoku-field-incorrect')
            self.assertFalse(submit_btn.is_enabled())
        
        # unsupported symbols (e.g. letters)
        write_value_in_field(input, 'a')
        self.assertEqual(input.get_attribute('value'), '')

        # delete all button
        # write sth in fields:
        ids = ('0_0', '2_3', '4_5', '6_2', '1_2')
        for id in ids:
            write_value_in_field(self.driver.find_element(by=By.ID, value=id), 2)
        # some fields are incorrect
        self.assertLess(0, len(self.driver.find_elements(by=By.CLASS_NAME, value='sudoku-field-incorrect')))
        # press button
        self.driver.find_element(by=By.ID, value='clear-sudoku-btn').click()
        # check
        for row in NINE_RANGE:
            for col in NINE_RANGE:
                self.assertEqual(self.driver.find_element(by=By.ID, value=f'{row}_{col}').get_attribute('value'), '')
                self.driver.implicitly_wait(0)
                self.assertEqual(0, len(self.driver.find_elements(by=By.CLASS_NAME, value='sudoku-field-incorrect')))
        self.driver.implicitly_wait(WAIT_TIME)

            

    def test_inputs_combined(self):
        """
        test whether the simple frontend checks are working correctly
        """

        submit_btn = self.driver.find_element(by=By.ID, value='submit-sudoku-btn')

        # row, column and block wise
        row_ids = ('0_0', '0_4', '0_8')
        column_ids = ('0_1', '4_1', '8_1')
        block_ids = ('6_6', '7_7', '8_8')
        field_value = FIELD_VALUE_MIN
        for id_list in [row_ids, column_ids, block_ids]:
            # get the input elements
            inputs: List[WebElement] = []
            for id in id_list:
                inputs.append(self.driver.find_element(by=By.ID, value=id))

            # write values into input elements and check if blocked
            for input in inputs:
                write_value_in_field(input, field_value)
            for input in inputs:
                self.assertEqual(input.get_attribute('class'), 'sudoku-field-incorrect')
            self.assertFalse(submit_btn.is_enabled())

            # remove all values but 1 and check if its free again
            inputs[1].clear()
            inputs[2].clear()
            for input in inputs:
                self.assertEqual(input.get_attribute('class'), '')
            self.assertTrue(submit_btn.is_enabled())

            field_value += 1

    def test_inputs_combined_2(self):
        """
        row, column and block all at once
        """
        field_value = 4
        submit_btn = self.driver.find_element(by=By.ID, value='submit-sudoku-btn')
        ids = ('0_5', '6_2', '2_1', '0_2')  # when the last field is set, all these fields should have an error
        inputs: List[WebElement] = []
        for id in ids:
            inputs.append(self.driver.find_element(by=By.ID, value=id))
        
        # set the first three fields and check that everything is alright
        for input in inputs[:-1]:
            write_value_in_field(input, field_value)

        self.assertTrue(submit_btn.is_enabled())
        for input in inputs:
            self.assertEqual(input.get_attribute('class'), '')

        # set the last field and check that everything is blocked:
        for input in inputs[-1:]:
            write_value_in_field(input, field_value)
            input.send_keys(Keys.TAB)
        
        self.assertFalse(submit_btn.is_enabled())
        for input in inputs:
            self.assertEqual(input.get_attribute('class'), 'sudoku-field-incorrect')
        
        # remove the last field and check that everything is alright again
        for input in inputs[-1:]:
            input.clear()
            input.send_keys(Keys.TAB)

        self.assertTrue(submit_btn.is_enabled())
        for input in inputs:
            self.assertEqual(input.get_attribute('class'), '')

    def test_modals(self):
        test_modals(self, self.driver, quickinfo=True, help=False)
