from selenium.webdriver.common.by import By

from base.mis.base_page import BasePage, BaseHandle


class HomePage(BasePage):

    def __init__(self):
        super().__init__()

        # 信息管理
        self.msg_manage = (By.LINK_TEXT, "信息管理")
        # 内容审核
        self.content_audit = (By.LINK_TEXT, "内容审核")

    def find_msg_mange(self):
        return self.find_element(self.msg_manage)

    def find_content_audit(self):
        return self.find_element(self.content_audit)


class HomeHandle(BaseHandle):

    def __init__(self):
        super().__init__()
        self.home_page = HomePage()

    def click_msg_manage(self):
        self.home_page.find_msg_mange().click()

    def click_content_audit(self):
        self.home_page.find_content_audit().click()


class HomeProxy:

    def __init__(self):
        self.home_handle = HomeHandle()

    # 进入文章审核页面
    def to_article_auidt_page(self):
        self.home_handle.click_msg_manage()
        self.home_handle.click_content_audit()
