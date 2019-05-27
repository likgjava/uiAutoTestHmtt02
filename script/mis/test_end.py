from utils import DriverUtil

import pytest


@pytest.mark.run(order=199)
class TestEnd:

    def test_end(self):
        # 打开自动退出的开关
        DriverUtil.set_mis_auto_quit(True)
        DriverUtil.quit_mis_driver()
