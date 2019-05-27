import time

import pytest

from utils import DriverUtil


@pytest.mark.run(order=299)
class TestEnd:

    def test_login(self):
        time.sleep(5)
        DriverUtil.set_app_auto_quit(True)
        DriverUtil.quit_app_driver()
