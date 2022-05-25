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


class TestHiddenSingle(ut.TestCase):
    """
    the Tests for the Hidden Single Algorithm Page
    """
    driver: WebDriver = None

    def setUp(self) -> None:
        self.driver = start_driver(get_page_sub_url('hidden_single'))

    def tearDown(self) -> None:
        quit_driver(self.driver)
        self.driver = None

    def test_hidden_single(self):
        gt = GeneralTests(self.driver, self)
        gt.step_1()

        gt.nxt_hint_btn.click()

        gt.step_2()

        gt.nxt_hint_btn.click()

        gt.step_3(use=1) # TODO: Delete = True

        gt.nxt_hint_btn.click()

        gt.step_4(new=1) # TODO: Delete = True
