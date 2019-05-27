import time

import utils
from page.mp.home_page import HomeProxy
from page.mp.publish_page import PublishProxy
from utils import DriverUtil
import pytest


import pytest


@pytest.mark.run(order=3)
class TestPublish:

    def setup_class(self):
        self.driver = DriverUtil.get_mp_driver()
        self.home_proxy = HomeProxy()
        self.publish_proxy = PublishProxy()

    def setup(self):
        time.sleep(2)

    def teardown_class(self):
        DriverUtil.quit_mp_driver()

    def test_publish(self):
        # 进入文章发布页面
        self.home_proxy.to_publish_article_page()

        # 发布文章
        self.publish_proxy.publish_article("test0005", "文章内容...", "软件测试")

        # 断言
        is_exist = utils.exist_text(self.driver, "新增文章成功")
        assert is_exist
