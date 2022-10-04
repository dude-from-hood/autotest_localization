# write a test that verifies that the product page on the site contains a button "add to basket" here.
# using fixtures here from conftest.py

from selenium.webdriver.common.by import By
import time


def test_page_has_button_add_to_basket(browser):
    browser.get(
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    browser.implicitly_wait(1)
    browser.find_elements(By.CSS_SELECTOR, "#login_link")
    buttonBasket = browser.find_element(
        By.CSS_SELECTOR, "[class~='btn-add-to-basket']")
    assert buttonBasket, 'Селектор кнопки не найден'
    buttonBasket.click()
    time.sleep(3)
