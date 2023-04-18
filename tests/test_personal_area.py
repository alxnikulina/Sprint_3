from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import (
    MainPage,
    Urls,
    LoginPageLocators,
)


class TestLoginPage:
    def test_enter_profile_settings(self, chrome_driver):
        chrome_driver.get(Urls.main_page_url)
        chrome_driver.find_element(By.XPATH, MainPage.my_profile_button).click()
        login_header = WebDriverWait(chrome_driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, LoginPageLocators.login_header)
            )
        )
        assert login_header
