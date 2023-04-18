from selenium.webdriver.common.by import By
from locators_for_tests import locators


class TestAuthentication:
    def test_to_enter_a_personal_area (self, chrome_driver):
        chrome_driver.get(locators["site"])
        chrome_driver.find_element(By.XPATH, locators["personal_area"]).click()
        