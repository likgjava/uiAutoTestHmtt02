import time

import pytest

import utils
from page.mp.login_page import LoginProxy
from utils import DriverUtil

import pytest


@pytest.mark.run(order=2)
class TestLogin:

    def setup_class(self):
        self.login_proxy = LoginProxy()

    def setup(self):
        time.sleep(2)

    def teardown_class(self):
        DriverUtil.quit_mp_driver()

    def test_login(self):
        # 测试数据
        username = "13041092162"
        code = "123456"

        # 登录
        self.login_proxy.login(username, code)

        # 断言
        is_exist = utils.exist_text(DriverUtil.get_mp_driver(), username)
        assert is_exist
