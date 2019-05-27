import time

import pytest

from page.mis.article_audit_page import ArticleAuditProxy
from page.mis.home_page import HomeProxy
from utils import DriverUtil


@pytest.mark.run(order=103)
class TestArticleAudit:

    def setup_class(self):
        self.driver = DriverUtil.get_mis_driver()
        self.home_proxy = HomeProxy()
        self.article_audit_proxy = ArticleAuditProxy()

    def setup(self):
        time.sleep(2)

    def teardown_class(self):
        DriverUtil.quit_mis_driver()

    def test_article_audit(self):
        # 测试数据
        title = "test0007"
        status = "待审核"

        # 进入文章审核页面
        self.home_proxy.to_article_auidt_page()

        # 审核
        self.article_audit_proxy.article_audit(title, status)

        time.sleep(10)

        # 断言
        is_audit_pass = self.article_audit_proxy.is_audit_pass(title)
        assert is_audit_pass

        time.sleep(10)
