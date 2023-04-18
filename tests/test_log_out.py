from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import MainPage, Urls, LoginPageLocators, ProfilePageLocators


class TestLogOut:
    def test_log_out(self, chrome_driver):
        chrome_driver.get(Urls.login_url)
        chrome_driver.find_element(By.XPATH, LoginPageLocators.email_input).send_keys(
            "Nikulina_alexandra_8_spint_3@yandex.ru"
        )
        chrome_driver.find_element(
            By.XPATH, LoginPageLocators.password_input
        ).send_keys("Al25ki06")
        chrome_driver.find_element(By.XPATH, LoginPageLocators.login_button).click()
        chrome_driver.find_element(By.XPATH, MainPage.my_profile_button).click()
        WebDriverWait(chrome_driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, ProfilePageLocators.logout_button)
            )
        ).click()
        login_header = WebDriverWait(chrome_driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, LoginPageLocators.login_header)
            )
        )
        assert login_header
