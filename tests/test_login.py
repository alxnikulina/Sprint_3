from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import (
    MainPage,
    Urls,
    LoginPageLocators,
    ForgotPasswordPageLocators,
)


class TestLogin:
    def test_login_from_account_page(self, chrome_driver):
        chrome_driver.get(Urls.main_page_url)
        chrome_driver.find_element(By.XPATH, MainPage.my_profile_button).click()
        chrome_driver.find_element(By.XPATH, LoginPageLocators.email_input).send_keys(
            "Nikulina_alexandra_8_spint_3@yandex.ru"
        )
        chrome_driver.find_element(
            By.XPATH, LoginPageLocators.password_input
        ).send_keys("Al25ki06")
        chrome_driver.find_element(By.XPATH, LoginPageLocators.login_button).click()
        WebDriverWait(chrome_driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, MainPage.my_profile_button)
            )
        ).click()
        profile_button = WebDriverWait(chrome_driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, MainPage.my_profile_button)
            )
        )
        assert profile_button

    def test_login_from_restore_password(self, chrome_driver):
        chrome_driver.get(Urls.main_page_url)
        chrome_driver.find_element(By.XPATH, MainPage.my_profile_button).click()
        chrome_driver.find_element(
            By.XPATH, LoginPageLocators.restore_password_button
        ).click()
        chrome_driver.find_element(
            By.XPATH, ForgotPasswordPageLocators.login_button
        ).click()
        chrome_driver.find_element(By.XPATH, LoginPageLocators.email_input).send_keys(
            "Nikulina_alexandra_8_spint_3@yandex.ru"
        )
        chrome_driver.find_element(
            By.XPATH, LoginPageLocators.password_input
        ).send_keys("Al25ki06")
        chrome_driver.find_element(By.XPATH, LoginPageLocators.login_button).click()
        WebDriverWait(chrome_driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, MainPage.my_profile_button)
            )
        ).click()
        profile_button = WebDriverWait(chrome_driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, MainPage.my_profile_button)
            )
        )
        assert profile_button
