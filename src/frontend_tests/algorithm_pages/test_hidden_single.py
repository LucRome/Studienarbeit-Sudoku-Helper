import unittest as ut
from selenium.webdriver.firefox.webdriver import WebDriver

from ..utils.web_driver_utils import start_driver, quit_driver
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
