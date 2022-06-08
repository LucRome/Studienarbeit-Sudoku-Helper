import unittest as ut
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from typing import List

from ..utils.modal_tests import test_modals
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


    def step_3(self, use=0, use_b=False, lock=0, lock_b=False, delete=False):
        """
        tests for step 3
        :param use: the amount of Candidates that are marked to be used  
        :param use_b: are candidates marked to be used? (Use when exact amount isnt given)
        :param lock: the amount of Candidates that are marked to be locked  
        :param use: the amount of Candidates that are marked to be used  
        :param lock_b: are candidates marked to be locked? (Use when exact amount isnt given)
        :param delete: are candidates marked to be deleted
        """
        # quickinfo for step 3
        self.tc.assertTrue(self.q_i_s3.is_displayed() and not self.q_i_s1.is_displayed())
         # next step button is available
        self.tc.assertTrue(self.nxt_hint_btn.is_displayed())
        self.tc.assertFalse(self.comp_cands_btn.is_displayed())

        # (+ 1, > 1: because of Legend)
        if use_b:
            self.tc.assertLess(1, len(self.driver.find_elements(by=By.CSS_SELECTOR, value='img[src*="marked_use"')))
        else:
            self.tc.assertEqual(use + 1, len(self.driver.find_elements(by=By.CSS_SELECTOR, value='img[src*="marked_use"')))
        if lock_b:
            self.tc.assertLess(1, len(self.driver.find_elements(by=By.CSS_SELECTOR, value='img[src*="marked_lock"')))
        else:
            self.tc.assertEqual(lock + 1, len(self.driver.find_elements(by=By.CSS_SELECTOR, value='img[src*="marked_lock"')))
        if delete:
            self.tc.assertLess(1, len(self.driver.find_elements(by=By.CSS_SELECTOR, value='img[src*="marked_delete"')))
            


    def step_4(self, new=0, new_b=False, locked=0, locked_b=False, removed_n_locked=0, removed_n_locked_b=False, removed=False):
        """
        tests for step 4
        :param new: amount of fields with new value
        :param new_b: are there fields with new value? (use when exact amount isnt given)
        :param locked: amount of fields with locked candidates
        :param locked_b: are there fields with locked candidates? (use when exact amount isnt given)
        :param removed_n_locked: amount fo fields with locked and removed candidates
        :param removed_n_locked_b: are there fields with locked and removed candidates? (use when exact amount isnt given)
        :param removed: are there fields with removed candidates?
        """
        # quickinfo for step 4
        self.tc.assertTrue(self.q_i_s3.is_displayed() and not self.q_i_s1.is_displayed())
        # compute candidates button is available
        self.tc.assertFalse(self.nxt_hint_btn.is_displayed())
        self.tc.assertTrue(self.comp_cands_btn.is_displayed())

        # (+ 1, > 1: because of Legend)
        if new_b:
            self.tc.assertLess(1, len(self.driver.find_elements(by=By.CLASS_NAME, value='field-new-value')))
        else:
            self.tc.assertEqual(new + 1, len(self.driver.find_elements(by=By.CLASS_NAME, value='field-new-value')))
        if locked_b:
            self.tc.assertLess(1, len(self.driver.find_elements(by=By.CLASS_NAME, value='field-locked-candidates')))
        else:
            self.tc.assertEqual(locked + 1, len(self.driver.find_elements(by=By.CLASS_NAME, value='field-locked-candidates')))
        if removed_n_locked_b:
            self.tc.assertLess(1, len(self.driver.find_elements(by=By.CLASS_NAME, value='field-locked-and-removed-candidates')))
        else:
            self.tc.assertEqual(removed_n_locked + 1, len(self.driver.find_elements(by=By.CLASS_NAME, value='field-locked-and-removed-candidates')))
        if removed:
            self.tc.assertLess(1, len(self.driver.find_elements(by=By.CLASS_NAME, value='field-removed-candidate')))
