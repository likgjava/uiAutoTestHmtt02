from utils import DriverUtil


# 对象库层-父类
class BasePage:

    def __init__(self):
        self.driver = DriverUtil.get_mp_driver()

    # 查找元素
    def find_element(self, location):
        print("find_element location={}".format(location))
        return self.driver.find_element(location[0], location[1])


# 操作层-父类
class BaseHandle:

    # 输入文本内容
    def input_text(self, element, text):
        element.clear()
        element.send_keys(text)
