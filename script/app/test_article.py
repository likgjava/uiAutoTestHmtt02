import logging
import time

import pytest

from page.app.index_page import IndexProxy
from utils import DriverUtil
import json
import allure
import config


# 构建测试数据，读取json文件
def build_data():
    test_data = []
    with open(config.BASE_DIR + "/data/app/article.json", encoding="UTF-8") as f:
        data = json.load(f)
        for case_data in data:
            test_data.append((case_data.get("channel"), case_data.get("title")))
    print("test_data=", test_data)
    return test_data


@pytest.mark.run(order=201)
class TestArticle:

    def setup_class(self):
        self.driver = DriverUtil.get_app_driver()
        self.index_proxy = IndexProxy()

    def setup(self):
        pass

    def teardown_class(self):
        DriverUtil.quit_app_driver()

    @pytest.mark.parametrize("channel,title", build_data())
    def test_find_article(self, channel, title):
        logging.info("param channel={} title={}".format(channel, title))
        # allure.attach('my attach', 'Hello World')
        # 测试数据
        # channel = "数据库"
        # title = "test0007"

        # 切换到指定的tab页面
        self.index_proxy.to_channel_tab(channel)
        time.sleep(2)

        # 查找文章
        self.index_proxy.show_article(title)
        time.sleep(5)
