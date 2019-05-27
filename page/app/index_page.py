from selenium.webdriver.common.by import By

from base.app.base_page import BasePage, BaseHandle


class IndexPage(BasePage):
    def __init__(self):
        super().__init__()
        # tab页
        self.tab = (By.XPATH, "//android.widget.HorizontalScrollView/*[contains(@text, '{}')]")
        # tab区域
        self.tab_area = (By.CLASS_NAME, "android.widget.HorizontalScrollView")
        # 文章
        self.article = (By.XPATH, "//*[contains(@text, '{}')]")

    def find_tab(self, channel):
        location = (self.tab[0], self.tab[1].format(channel))
        return self.find_element_by_swipe_left(self.tab_area, location)

    def find_article(self, title):
        location = (self.article[0], self.article[1].format(title))
        return self.find_element(location)


class IndexHandle(BaseHandle):
    def __init__(self):
        self.index_page = IndexPage()

    # 切换到指定的频道
    def to_channel_tab(self, channel):
        self.index_page.find_tab(channel).click()

    def click_article(self, title):
        self.index_page.find_article(title).click()


class IndexProxy:
    def __init__(self):
        self.index_handle = IndexHandle()

    # 切换到指定的频道
    def to_channel_tab(self, channel):
        self.index_handle.to_channel_tab(channel)

    # 查看文章
    def show_article(self, title):
        self.index_handle.click_article(title)
