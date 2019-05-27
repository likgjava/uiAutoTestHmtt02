import time

import pytest

import utils
from page.mis.login_page import LoginProxy
from utils import DriverUtil

import pytest

@pytest.mark.run(order=102)
class TestLogin:

    def setup_class(self):
        self.driver = DriverUtil.get_mis_driver()
        self.login_proxy = LoginProxy()

    def setup(self):
        time.sleep(2)

    def teardown_class(self):
        DriverUtil.quit_mis_driver()

    def test_login(self):
        # 测试数据
        username = "testid"
        pwd = "testpwd123"

        # 登录
        self.login_proxy.login(username, pwd)

        # 断言
        is_exist = utils.exist_text(self.driver, "退出")
        assert is_exist
