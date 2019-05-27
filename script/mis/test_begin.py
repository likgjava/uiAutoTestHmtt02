from utils import DriverUtil
import pytest


@pytest.mark.run(order=101)
class TestBegin:

    def test_begin(self):
        # 关闭自动退出的开关
        DriverUtil.set_mis_auto_quit(False)
