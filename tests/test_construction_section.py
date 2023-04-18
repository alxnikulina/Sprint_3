from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import MainPage, Urls


class TestConstructionSection:
    def test_enter_to_construction_section(self, chrome_driver):
        chrome_driver.get(Urls.main_page_url)
        chrome_driver.find_element(By.XPATH, MainPage.my_profile_button).click()
        chrome_driver.find_element(By.XPATH, MainPage.constructor_logo).click()
        bun_section = WebDriverWait(chrome_driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, MainPage.bun_section)
            )
        )
        assert bun_section
