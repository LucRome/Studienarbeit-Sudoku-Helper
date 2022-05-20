import unittest as ut
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from typing import List

from ..utils.web_driver_utils import start_driver, quit_driver
from ..utils.input_utils import enter_sudoku, submit_sudoku, write_value_in_field, clear_all_fields
from backend.sudoku.base import ALL_FIELD_VALUES, FIELD_VALUE_MAX, FIELD_VALUE_MIN, NINE_RANGE
from ..utils.modal_tests import test_modals
from ..utils.waits import wait_for_page_to_load
from backend.dev_tools.algorithm_sudokus import NAME_MAP


class TestGeneral(ut.TestCase):
    """
    Test Cases which are usefull for all algorithm pages
    """
    driver: WebDriver = None

    def setUp(self) -> None:
        self.driver = start_driver()

    def tearDown(self) -> None:
        quit_driver(self.driver)
        self.driver = None


    def test_hint_steps(self):
        """
        iterates over the hints (for all algorithm pages)
        """
        # first enter sudoku
        enter_sudoku(self.driver, NAME_MAP['third_eye'])
        submit_sudoku(self.driver)

        # skip verified page
        self.driver.find_element(by=By.ID, value='solve-sudoku-btn').click()
        wait_for_page_to_load(self.driver, timeout=120, poll_frequency=5)

        # actual tests

        nxt_hint_btn = self.driver.find_element(by=By.ID, value='nxt-hint-btn')
        comp_cands_btn = self.driver.find_element(by=By.ID, value='solve-sudoku-btn')
        q_i_s1 = self.driver.find_element(by=By.CSS_SELECTOR, value='.quickinfo-step[step="1"]')
        q_i_s3 = self.driver.find_element(by=By.CSS_SELECTOR, value='.quickinfo-step[step="3"]')

        # Start: all candidates are hidden
        candidates = self.driver.find_elements(by=By.CLASS_NAME, value='candidate-table')
        self.assertGreater(len(candidates), 0)
        for can in candidates:
            self.assertFalse(can.is_displayed())
        # some fields are marked as affected
        self.assertGreater(len(self.driver.find_elements(by=By.CLASS_NAME, value='field-affected')), 0)
        # quickinfo for step 1
        self.assertTrue(q_i_s1.is_displayed() and not q_i_s3.is_displayed())
        # next step button is available
        self.assertTrue(nxt_hint_btn.is_displayed())
        self.assertFalse(comp_cands_btn.is_displayed())

        nxt_hint_btn.click()

        # Step 2: candidates are displayed
        for can in candidates:
            self.assertTrue(can.is_displayed())
        # quickinfo for step 1
        self.assertTrue(q_i_s1.is_displayed() and not q_i_s3.is_displayed())
        # next step button is available
        self.assertTrue(nxt_hint_btn.is_displayed())
        self.assertFalse(comp_cands_btn.is_displayed())

        nxt_hint_btn.click()

        # Step 3: 
        # quickinfo for step 3
        self.assertTrue(q_i_s3.is_displayed() and not q_i_s1.is_displayed())
         # next step button is available
        self.assertTrue(nxt_hint_btn.is_displayed())
        self.assertFalse(comp_cands_btn.is_displayed())

        nxt_hint_btn.click()

        # Step 4:
        # quickinfo for step 4
        self.assertTrue(q_i_s3.is_displayed() and not q_i_s1.is_displayed())
        # compute candidates button is available
        self.assertFalse(nxt_hint_btn.is_displayed())
        self.assertTrue(comp_cands_btn.is_displayed())