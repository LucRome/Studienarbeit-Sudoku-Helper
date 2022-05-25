import unittest as ut
from django.test import TestCase

from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By


def test_single_modal(tc: TestCase, driver: WebDriver, modal_id: str) -> None:
    modal = driver.find_element(by=By.ID, value=modal_id)
    tc.assertFalse(modal.is_displayed())
    # open modal
    driver.find_element(by=By.CSS_SELECTOR, value=f'[data-bs-target="#{modal_id}"]').click()
    tc.assertTrue(modal.is_displayed())
    # close modal
    modal.find_element(by=By.CSS_SELECTOR, value='[data-bs-dismiss=modal]').click()
    tc.assertFalse(modal.is_displayed())


def test_modals(tc: ut.TestCase, driver: WebDriver, quickinfo: bool, help: bool, settings: bool = False) -> None:
    """
    Tests whether the modals display correctly, doesn't test the content of the modals
    """

    if quickinfo:
        test_single_modal(tc, driver, 'quickinfo-modal')
    if help:
        test_single_modal(tc, driver, 'help-modal')
    if settings:
        test_single_modal(tc, driver, 'settings-modal')
