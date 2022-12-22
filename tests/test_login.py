from selenium import webdriver


class TestLoginUI:
    def test_title(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("https://demo.openemr.io/b/openemr")
        self.driver.execute_script()
        assert self.driver.title == "Google"
