from object.baseuse.base_func import BaseFunc
import time


class Login(BaseFunc):

    def login_page(self, username, password):
        user = '//input[@name="username"]'
        pwd = '//input[@name="password"]'
        submit = '//button[@type="submit"]'

        self.wait_until_visible(user)
        self.find_element(user).send_keys(username)
        self.find_element(pwd).send_keys(password)
        self.find_element(submit).click()
        time.sleep(5)
        from object.page.base_page.main_page import MainPage
        return MainPage(self.driver)
