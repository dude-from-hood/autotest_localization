# write a test that verifies that the product page on the site contains a button "add to basket" here.
# using fixtures here from conftest.py

from selenium.webdriver.common.by import By
import time


def test_content_should_display_by_chosen_language(browser):
    browser.get(
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    browser.implicitly_wait(1)
    browser.find_element(By.CSS_SELECTOR, "#login_link")
    buttonBasket = browser.find_element(
        By.CSS_SELECTOR, "[class~='btn-add-to-basket']")
    buttonBasket.click()
    time.sleep(3)
