from selenium.webdriver.common.by import By
from locators_for_tests import locators

class TestRegistration:
    def test_successful_registration(self, chrome_driver):
        chrome_driver.get(locators["register"])
        chrome_driver.find_element(By.XPATH, locators["name_placeholder"]).send_keys('Alexandra')
        chrome_driver.find_element(By.NAME, "Пароль").send_keys("Al25069393")
        chrome_driver.find_element(By.XPATH, locators["email_placeholder"]).send_keys("Nikulina_alexandra_8_spint_3@yandex.ru")
        chrome_driver.find_element(By.XPATH, locators["button"])
        chrome_driver.get(locators["login"])


    def test_unsuccessful_registration(self, chrome_driver):
        chrome_driver.get(locators["register"])
        chrome_driver.find_element(By.XPATH, locators["name_placeholder"]).send_keys('Kirill')
        chrome_driver.find_element(By.NAME, "Пароль").send_keys("Al23")
        chrome_driver.find_element(By.XPATH, locators["email_placeholder"]).send_keys("Nikulina_alexandra_8_spint_3@yandex.ru")
        chrome_driver.find_element(By.XPATH, locators["button"])
        chrome_driver.get(locators["login"])
        if "Страница" in chrome_driver.current_url:
            print("Регистрация успешна!")
        else:
            print("Регистрация провалилась(: ")