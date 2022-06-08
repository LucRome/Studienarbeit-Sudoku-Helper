import unittest as ut
from selenium.webdriver.firefox.webdriver import WebDriver

from ..utils.web_driver_utils import start_driver, quit_driver
from .utils import get_page_sub_url
from .general_tests import GeneralTests


class TestSwordfishFin(ut.TestCase):
    """
    the Tests for the finned swordfish Algorithm Page
    """
    driver: WebDriver = None

    def test_swordfish_fin_col(self):
        self.driver = start_driver(get_page_sub_url('swordfish_fin_col'))
        gt = GeneralTests(self.driver, self)
        gt.step_1()

        gt.nxt_hint_btn.click()

        gt.step_2()

        gt.nxt_hint_btn.click()

        gt.step_3(lock_b=True, delete=True)

        gt.nxt_hint_btn.click()

        gt.step_4(locked_b=True, removed=True)

    def test_swordfish_fin_row(self):
        self.driver = start_driver(get_page_sub_url('swordfish_fin_row'))
        gt = GeneralTests(self.driver, self)
        gt.step_1()

        gt.nxt_hint_btn.click()

        gt.step_2()

        gt.nxt_hint_btn.click()

        gt.step_3(lock_b=True, delete=True)

        gt.nxt_hint_btn.click()

        gt.step_4(locked_b=True, removed=True)
