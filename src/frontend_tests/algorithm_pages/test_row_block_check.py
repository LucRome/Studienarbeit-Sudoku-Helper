import unittest as ut
from selenium.webdriver.firefox.webdriver import WebDriver

from ..utils.web_driver_utils import start_driver, quit_driver
from .utils import get_page_sub_url
from .general_tests import GeneralTests


class TestRowBlockCheck(ut.TestCase):
    """
    the Tests for the Row-Block-Check Algorithm Page
    """
    driver: WebDriver = None

    def setUp(self) -> None:
        self.driver = start_driver(get_page_sub_url('row_block_check'))

    def tearDown(self) -> None:
        quit_driver(self.driver)
        self.driver = None

    def test_row_block_check(self):
        gt = GeneralTests(self.driver, self)
        gt.step_1()

        gt.nxt_hint_btn.click()

        gt.step_2()

        gt.nxt_hint_btn.click()

        gt.step_3(lock_b=True, delete=True)

        gt.nxt_hint_btn.click()

        gt.step_4(locked_b=True, removed=True)
