import time

from selenium.webdriver.common.by import By

import utils
from base.mis.base_page import BasePage, BaseHandle
from utils import DriverUtil


class ArticleAuditPage(BasePage):
    def __init__(self):
        super().__init__()

        # 标题
        self.title = (By.XPATH, "//input[contains(@placeholder, '文章名称')]")
        # 文章状态
        # 查询
        self.query_btn = (By.CLASS_NAME, "find")
        # 通过
        self.pass_btn = (By.XPATH, "//span[text()='通过']/..")
        # 确定按钮
        self.confirm_btn = (By.CLASS_NAME, "el-button--primary")

    def find_title(self):
        return self.find_element(self.title)

    def find_query_btn(self):
        return self.find_element(self.query_btn)

    def find_pass_btn(self):
        return self.find_element(self.pass_btn)

    def find_confirm_btn(self):
        return self.find_element(self.confirm_btn)


class ArticleAuditHandle(BaseHandle):
    def __init__(self):
        super().__init__()
        self.driver = DriverUtil.get_mis_driver()
        self.article_audit_page = ArticleAuditPage()

    def input_title(self, title):
        self.input_text(self.article_audit_page.find_title(), title)

    def select_audit_status(self, status):
        utils.select_item(self.driver, "请选择状态", status)

    def click_query_btn(self):
        self.article_audit_page.find_query_btn().click()

    def click_pass_btn(self):
        self.article_audit_page.find_pass_btn().click()

    def click_confirm_btn(self):
        self.article_audit_page.find_confirm_btn().click()


class ArticleAuditProxy:
    def __init__(self):
        self.driver = DriverUtil.get_mis_driver()
        self.article_audit_handle = ArticleAuditHandle()

    # 文章审核
    def article_audit(self, title, status):
        self.article_audit_handle.input_title(title)
        self.article_audit_handle.select_audit_status(status)
        self.article_audit_handle.click_query_btn()
        time.sleep(2)
        self.article_audit_handle.click_pass_btn()
        self.article_audit_handle.click_confirm_btn()


    # 判断文章是否为审核通过
    def is_audit_pass(self, title):
        self.driver.refresh()
        self.article_audit_handle.input_title(title)
        self.article_audit_handle.select_audit_status("审核通过")
        self.article_audit_handle.click_query_btn()
        return utils.exist_text(self.driver, title)
