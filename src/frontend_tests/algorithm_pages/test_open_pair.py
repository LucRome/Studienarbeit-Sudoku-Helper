import unittest as ut
from selenium.webdriver.firefox.webdriver import WebDriver

from ..utils.web_driver_utils import start_driver, quit_driver
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

    def test_open_pair(self):
        gt = GeneralTests(self.driver, self)
        gt.step_1()

        gt.nxt_hint_btn.click()

        gt.step_2()

        gt.nxt_hint_btn.click()

        gt.step_3(lock=4, delete=True)

        gt.nxt_hint_btn.click()

        gt.step_4(locked=2, removed=True)
