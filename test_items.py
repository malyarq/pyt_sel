import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_is_btn_add_to_basket_exist(browser):
    browser.get(link)
    def exist():
        try:
            browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
        except NoSuchElementException:
            return False
        return True
    assert exist(), "Button doesn't exist on this page"