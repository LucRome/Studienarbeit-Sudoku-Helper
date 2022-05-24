import unittest as ut
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.remote.webelement import WebElement
from typing import List

from ..utils.web_driver_utils import start_driver, quit_driver
from ..utils.input_utils import enter_sudoku, submit_sudoku, write_value_in_field, clear_all_fields
from backend.sudoku.base import ALL_FIELD_VALUES, FIELD_VALUE_MAX, FIELD_VALUE_MIN, NINE_RANGE
from ..utils.modal_tests import test_modals
from ..utils.waits import wait_for_page_to_load
from backend.dev_tools.algorithm_sudokus import NAME_MAP
from ..utils.modal_tests import test_modals


class GeneralTests:
    """
    Test Cases which are usefull for all algorithm pages \n
    !Only initialise when the algorithm Page has loaded!
    """
    nxt_hint_btn: WebElement
    comp_cands_btn: WebElement
    q_i_s1: WebElement
    q_i_s3: WebElement
    driver: WebDriver
    tc: ut.TestCase
    candidates: List[WebElement]

    def __init__(self, driver: WebDriver, tc: ut.TestCase) -> None:
        self.tc = tc
        self.driver = driver
        self.nxt_hint_btn = self.driver.find_element(by=By.ID, value='nxt-hint-btn')
        self.comp_cands_btn = self.driver.find_element(by=By.ID, value='solve-sudoku-btn')
        self.q_i_s1 = self.driver.find_element(by=By.CSS_SELECTOR, value='.quickinfo-step[step="1"]')
        self.q_i_s3 = self.driver.find_element(by=By.CSS_SELECTOR, value='.quickinfo-step[step="3"]')


    def step_1(self):
        """
        tests for step 1
        """
        # Start: all candidates are hidden
        self.candidates = self.driver.find_elements(by=By.CLASS_NAME, value='candidate-table')
        self.tc.assertGreater(len(self.candidates), 0)
        for can in self.candidates:
            self.tc.assertFalse(can.is_displayed())
        # some fields are marked as affected
        self.tc.assertGreater(len(self.driver.find_elements(by=By.CLASS_NAME, value='field-affected')), 0)
        # quickinfo for step 1
        self.tc.assertTrue(self.q_i_s1.is_displayed() and not self.q_i_s3.is_displayed())
        # next step button is available
        self.tc.assertTrue(self.nxt_hint_btn.is_displayed())
        self.tc.assertFalse(self.comp_cands_btn.is_displayed())
        # test modals
        test_modals(self.tc, self.driver, quickinfo=True, help=True)


    def step_2(self):
        """
        tests for step 2
        """
        # candidates are displayed
        for can in self.candidates:
            self.tc.assertTrue(can.is_displayed())
        # quickinfo for step 1
        self.tc.assertTrue(self.q_i_s1.is_displayed() and not self.q_i_s3.is_displayed())
        # next step button is available
        self.tc.assertTrue(self.nxt_hint_btn.is_displayed())
        self.tc.assertFalse(self.comp_cands_btn.is_displayed())


    def step_3(self, use = 0, lock=0, delete=False):
        """
        tests for step 3
        """
        # quickinfo for step 3
        self.tc.assertTrue(self.q_i_s3.is_displayed() and not self.q_i_s1.is_displayed())
         # next step button is available
        self.tc.assertTrue(self.nxt_hint_btn.is_displayed())
        self.tc.assertFalse(self.comp_cands_btn.is_displayed())

        # (+ 1, > 1: because of Legend)
        if use > 0:
            self.tc.assertEqual(use + 1, len(self.driver.find_elements(by=By.CSS_SELECTOR, value='img[src*="marked_use"')))
        if lock > 0:
            self.tc.assertEqual(lock + 1, len(self.driver.find_elements(by=By.CSS_SELECTOR, value='img[src*="marked_lock"')))
        if delete:
            self.tc.assertLess(1, len(self.driver.find_elements(by=By.CSS_SELECTOR, value='img[src*="marked_delete"')))
            


    def step_4(self, new=0, locked=0, removed_n_locked=0, removed=False):
        """
        tests for step 4
        """
        # quickinfo for step 4
        self.tc.assertTrue(self.q_i_s3.is_displayed() and not self.q_i_s1.is_displayed())
        # compute candidates button is available
        self.tc.assertFalse(self.nxt_hint_btn.is_displayed())
        self.tc.assertTrue(self.comp_cands_btn.is_displayed())

        # (+ 1, > 1: because of Legend)
        if new > 0:
            self.tc.assertEqual(new + 1, len(self.driver.find_elements(by=By.CLASS_NAME, value='field-new-value')))
        if locked > 0:
            self.tc.assertEqual(3, len(self.driver.find_elements(by=By.CLASS_NAME, value='field-locked-candidates')))
        if removed_n_locked > 0:
            self.tc.assertEqual(3, len(self.driver.find_elements(by=By.CLASS_NAME, value='field-locked-and-removed-candidates')))
        if removed:
            self.tc.assertLess(1, len(self.driver.find_elements(by=By.CLASS_NAME, value='field-removed-candidate')))
