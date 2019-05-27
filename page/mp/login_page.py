from selenium.webdriver.common.by import By

from base.mp.base_page import BasePage, BaseHandle


class LoginPage(BasePage):
    def __init__(self):
        super().__init__()

        # 用户名
        self.username = (By.CSS_SELECTOR, "[placeholder='请输入手机号']")
        # 验证码
        self.code = (By.CSS_SELECTOR, "[placeholder='验证码']")
        # 登录按钮
        self.login_btn = (By.CLASS_NAME, "el-button--primary")

    def find_username(self):
        return self.find_element(self.username)

    def find_code(self):
        return self.find_element(self.code)

    def find_login_btn(self):
        return self.find_element(self.login_btn)


class LoginHandle(BaseHandle):
    def __init__(self):
        self.login_page = LoginPage()

    def input_username(self, username):
        self.input_text(self.login_page.find_username(), username)

    def input_code(self, code):
        self.input_text(self.login_page.find_code(), code)

    def click_login_btn(self):
        self.login_page.find_login_btn().click()


class LoginProxy:
    def __init__(self):
        self.login_handle = LoginHandle()

    # 登录
    def login(self, username, code):
        self.login_handle.input_username(username)
        self.login_handle.input_code(code)
        self.login_handle.click_login_btn()
