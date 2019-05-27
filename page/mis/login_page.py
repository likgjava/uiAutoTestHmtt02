from selenium.webdriver.common.by import By

from base.mis.base_page import BasePage, BaseHandle
from utils import DriverUtil


class LoginPage(BasePage):
    def __init__(self):
        super().__init__()

        # 用户名
        self.username = (By.NAME, "username")
        # 密码
        self.pwd = (By.NAME, "password")
        # 登录按钮
        self.login_btn = (By.ID, "inp1")

    def find_username(self):
        return self.find_element(self.username)

    def find_pwd(self):
        return self.find_element(self.pwd)

    def find_login_btn(self):
        return self.find_element(self.login_btn)


class LoginHandle(BaseHandle):
    def __init__(self):
        self.login_page = LoginPage()

    def input_username(self, username):
        self.input_text(self.login_page.find_username(), username)

    def input_pwd(self, pwd):
        self.input_text(self.login_page.find_pwd(), pwd)

    def click_login_btn(self):
        self.login_page.find_login_btn().click()


class LoginProxy:
    def __init__(self):
        self.login_handle = LoginHandle()

    # 登录
    def login(self, username, pwd):
        self.login_handle.input_username(username)
        self.login_handle.input_pwd(pwd)
        js = 'document.getElementById("inp1").removeAttribute("disabled")'
        DriverUtil.get_mis_driver().execute_script(js)
        self.login_handle.click_login_btn()

