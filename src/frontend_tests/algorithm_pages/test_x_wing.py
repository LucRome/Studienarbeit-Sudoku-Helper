import unittest as ut
from selenium.webdriver.firefox.webdriver import WebDriver

from ..utils.web_driver_utils import start_driver, quit_driver
from .utils import get_page_sub_url
from .general_tests import GeneralTests


class TestXWing(ut.TestCase):
    """
    the Tests for the X-Wing Algorithm Page
    """
    driver: WebDriver = None
    driver2: WebDriver = None

    def tearDown(self) -> None:
        quit_driver(self.driver)
        self.driver = None
        quit_driver(self.driver2)
        self.driver2 = None

    def test_x_wing_row(self):
        self.driver = start_driver(get_page_sub_url('x_wing_row'))
        # row
        gt1 = GeneralTests(self.driver, self)
        gt1.step_1()

        gt1.nxt_hint_btn.click()

        gt1.step_2()

        gt1.nxt_hint_btn.click()

        gt1.step_3(lock=4, delete=True)

        gt1.nxt_hint_btn.click()

        gt1.step_4(locked=4, removed=True)

    def test_x_wing_col(self):
        self.driver = start_driver(get_page_sub_url('x_wing_col'))
        gt2 = GeneralTests(self.driver, self)
        gt2.step_1()

        gt2.nxt_hint_btn.click()

        gt2.step_2()

        gt2.nxt_hint_btn.click()

        gt2.step_3(lock=4, delete=True)

        gt2.nxt_hint_btn.click()

        gt2.step_4(locked=4, removed=True)
