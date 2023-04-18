import uuid
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Urls, SignUpPageLocators, LoginPageLocators


class TestSignUp:
    def test_successful_registration(self, chrome_driver):
        chrome_driver.get(Urls.sign_up_url)
        unique_email = str(uuid.uuid4())[:5] + "@yandex.ru"
        unique_name = str(uuid.uuid4())[:5]
        unique_password = str(uuid.uuid4())[:8]
        chrome_driver.find_element(By.XPATH, SignUpPageLocators.email_input).send_keys(
            unique_email
        )
        chrome_driver.find_element(By.XPATH, SignUpPageLocators.name_input).send_keys(
            unique_name
        )
        chrome_driver.find_element(
            By.XPATH, SignUpPageLocators.password_input
        ).send_keys(unique_password)
        chrome_driver.find_element(By.XPATH, SignUpPageLocators.sign_up_button).click()
        login_header = WebDriverWait(chrome_driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, LoginPageLocators.login_header)
            )
        )
        assert login_header

    def test_user_already_exists(self, chrome_driver):
        chrome_driver.get(Urls.sign_up_url)
        chrome_driver.find_element(By.XPATH, SignUpPageLocators.email_input).send_keys(
            "Nikulina_alexandra_8_spint_3@yandex.ru"
        )
        chrome_driver.find_element(By.XPATH, SignUpPageLocators.name_input).send_keys(
            "Александра"
        )
        chrome_driver.find_element(
            By.XPATH, SignUpPageLocators.password_input
        ).send_keys("Al25ki06")
        chrome_driver.find_element(By.XPATH, SignUpPageLocators.sign_up_button).click()
        user_already_exists_notification = WebDriverWait(chrome_driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, SignUpPageLocators.user_already_exists_notification)
            )
        )
        assert user_already_exists_notification
