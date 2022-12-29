import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from basee_conf.webdriver_listner import WebDriveWrapper
from utilities import data_source


class TestValidLogin(WebDriveWrapper):
    @pytest.mark.parametrize("username, password, language, expected_title", data_source.test_data)
    def test_valid_login(self, username, password, language, expected_title):
        self.driver.find_element(By.NAME, "authUser").send_keys(username)
        self.driver.find_element(By.ID, "clearPass").send_keys(password)
        select_lang = Select(self.driver.find_element(By.XPATH, "//select[@name='languageChoice']"))
        select_lang.select_by_visible_text(language)
        self.driver.find_element(By.ID, "login-button").location_once_scrolled_into_view
        self.driver.find_element(By.ID, "login-button").click()
        # calender_heading = self.driver.find_element(By.XPATH, "//div[contains(@class,'tabSpan bgcolor2')]").text
        # print("calender .....", calender_heading)
        # self.driver.switch_to.frame(self.driver.find_element(By.NAME, "cal"))
        # calender_month = self.driver.find_element(By.XPATH, "//td[text(), 'December']")
        # print("calender_month-----", calender_month)
        # self.driver.find_element(By.XPATH, "//span[text(),'Calender']")
        assert_that(self.driver.title).is_equal_to(expected_title)

    @pytest.mark.parametrize("username, password, language, expected_title", data_source.test_invalid_data)
    def test_invalid_login(self, username, password, language, expected_title):
        self.driver.find_element(By.NAME, "authUser").send_keys(username)
        self.driver.find_element(By.ID, "clearPass").send_keys(password)
        select_lang = Select(self.driver.find_element(By.XPATH, "//select[@name='languageChoice']"))
        select_lang.select_by_visible_text(language)
        self.driver.find_element(By.ID, "login-button").location_once_scrolled_into_view
        invalid_login = self.driver.find_element(By.XPATH, "//div[contains(text(),'Invalid')]").text
        self.driver.find_element(By.ID, "login-button").click()
        print("assert....", invalid_login)
        assert_that(invalid_login).contains("Invalid")
        assert_that(expected_title).does_not_match(self.driver.title)



class TestLoginUI(WebDriveWrapper):

    def test_title(self):
        assert_that("OpenEMR Login").is_equal_to(self.driver.title)

    def test_that_desc(self):
        actual_desc = self.driver.find_element(By.XPATH, "//p[contains(text(),'most')]").text
        print(actual_desc)
        assert_that(actual_desc).contains("Electronic Health Record and Medical Practice Management solution")

    def test_place_holder(self):
        placeholder_username = self.driver.find_element(By.ID, "authUser").get_attribute("placeholder")
        placeholder_password = self.driver.find_element(By.ID, "clearPass").get_attribute("placeholder")
        assert_that(placeholder_username).is_equal_to("Username") and assert_that(placeholder_password).is_equal_to(
            "Password")

