from selenium.common.exceptions import NoSuchElementException

from utils import DriverUtil
import logging


# 对象库层-父类
class BasePage:

    def __init__(self):
        self.driver = DriverUtil.get_app_driver()

    # 查找元素
    def find_element(self, location):
        logging.info("location={}".format(location))
        return self.driver.find_element(location[0], location[1])

    def find_element_by_swipe_left(self, swipe_area_location, target_location):
        # 计算滑动起始坐标
        area_ele = self.find_element(swipe_area_location)
        x = area_ele.location["x"]
        y = area_ele.location["y"]
        width = area_ele.size["width"]
        height = area_ele.size["height"]
        start_x = x + 0.75 * width
        start_y = y + 0.5 * height
        end_x = x + 0.25 * width
        end_y = start_y

        pre_page_source = self.driver.page_source
        while True:
            # 首先查找一次
            try:
                ele = self.find_element(target_location)
            except Exception as e:
                print("未找到...")
            else:
                print("找到了！")
                return ele

            # 向左滑动一下
            self.driver.swipe(start_x, start_y, end_x, end_y, 3000)

            # 判断是否滑动到页面的最右端了
            if pre_page_source == self.driver.page_source:
                print("滑动到最右端也没有找到元素")
                raise NoSuchElementException
            else:
                pre_page_source = self.driver.page_source


# 操作层-父类
class BaseHandle:

    # 输入文本内容
    def input_text(self, element, text):
        element.clear()
        element.send_keys(text)
