from utils import DriverUtil

import pytest


@pytest.mark.run(order=99)
class TestEnd:

    def test_end(self):
        # 打开自动退出的开关
        DriverUtil.set_mp_auto_quit(True)
        DriverUtil.quit_mp_driver()
