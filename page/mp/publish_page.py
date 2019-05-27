from selenium.webdriver.common.by import By

import utils
from base.mp.base_page import BasePage, BaseHandle
from utils import DriverUtil


class PublishPage(BasePage):
    def __init__(self):
        super().__init__()

        # 标题
        self.title = (By.CSS_SELECTOR, "[placeholder='文章名称']")
        # 内容iframe
        self.content_frame = (By.ID, "publishTinymce_ifr")
        # 内容
        self.content = (By.TAG_NAME, "body")
        # 封面
        self.cover = (By.XPATH, "//span[text()='自动']")
        # 频道
        self.channel = (By.CSS_SELECTOR, "[placeholder='请选择']")
        # 频道-数据库
        self.channel_db = (By.XPATH, "//*[text()='数据库']")
        # 发表
        self.publish_btn = (By.CLASS_NAME, "el-button--primary")

    def find_title(self):
        return self.find_element(self.title)

    def find_content_frame(self):
        return self.find_element(self.content_frame)

    def find_content(self):
        return self.find_element(self.content)

    def find_cover(self):
        return self.find_element(self.cover)

    def find_channel(self):
        return self.find_element(self.channel)

    def find_channel_db(self):
        return self.find_element(self.channel_db)

    def find_publish_btn(self):
        return self.find_element(self.publish_btn)


class PublishHandle(BaseHandle):
    def __init__(self):
        self.publish_page = PublishPage()
        self.driver = DriverUtil.get_mp_driver()

    def input_title(self, title):
        self.input_text(self.publish_page.find_title(), title)

    def input_content(self, content):
        # frame切换
        self.driver.switch_to.frame(self.publish_page.find_content_frame())
        self.input_text(self.publish_page.find_content(), content)
        self.driver.switch_to.default_content()

    def click_cover(self):
        self.publish_page.find_cover().click()

    def select_channel(self, channel_name):
        # self.publish_page.find_channel().click()
        # self.publish_page.find_channel_db().click()
        utils.select_item(self.driver, "请选择", channel_name)

    def click_publish_btn(self):
        self.publish_page.find_publish_btn().click()


class PublishProxy:
    def __init__(self):
        self.publish_handle = PublishHandle()

    # 发布文章
    def publish_article(self, title, content, channel):
        self.publish_handle.input_title(title)
        self.publish_handle.input_content(content)
        self.publish_handle.click_cover()
        self.publish_handle.select_channel(channel)
        self.publish_handle.click_publish_btn()
