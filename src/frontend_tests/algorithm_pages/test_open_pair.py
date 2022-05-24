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
from .utils import get_page_sub_url
from .general_tests import GeneralTests


class TestOpenPair(ut.TestCase):
    """
    the Tests for the Open Pair Algorithm Page
    """
    driver: WebDriver = None

    def setUp(self) -> None:
        self.driver = start_driver(get_page_sub_url('open_pair'))

    def tearDown(self) -> None:
        quit_driver(self.driver)
        self.driver = None

    def test_open_single(self):
        gt = GeneralTests(self.driver, self)
        gt.step_1()

        gt.nxt_hint_btn.click()

        gt.step_2()

        gt.nxt_hint_btn.click()

        gt.step_3()
        # 4 candidates are marked lock (+ 1 from Legend)
        self.assertEqual(5, len(self.driver.find_elements(by=By.CSS_SELECTOR, value='img[src*="marked_lock"')))
        # multiple candidates are marked delete (+ 1 from Legend)
        self.assertLess(1, len(self.driver.find_elements(by=By.CSS_SELECTOR, value='img[src*="marked_delete"')))

        gt.nxt_hint_btn.click()

        gt.step_4()
        # 2 fields have locked candidates (+ the field in the legend)
        self.assertEqual(3, len(self.driver.find_elements(by=By.CLASS_NAME, value='field-locked-candidates')))
        # fields have lost candidates (+ 1 from Legend)
        self.assertLess(1, len(self.driver.find_elements(by=By.CLASS_NAME, value='field-removed-candidate')))
