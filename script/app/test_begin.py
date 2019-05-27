import pytest

from utils import DriverUtil


@pytest.mark.run(order=200)
class TestBegin:

    def test_login(self):
        DriverUtil.set_app_auto_quit(False)
