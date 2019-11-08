import selenium.webdriver
import appium.webdriver

# 处理下拉框
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


def select_item(driver, placeholder, value):
    print("1111111111")
    # 点击下拉框
    driver.find_element_by_xpath("//*[@placeholder='{}']".format(placeholder)).click()

    # 获取所有的选项
    item_list = driver.find_elements_by_css_selector("ul.el-scrollbar__view li")

    # 遍历、对比
    is_exist = False
    for item in item_list:
        print("item.text==", item.text)
        if value == item.text:
            is_exist = True
            item.click()
            print("找到了...")
            break

        # 点击键盘的向下的方向键
        ActionChains(driver).move_to_element(item).send_keys(Keys.DOWN).perform()

    # 遍历了一边，都没有找到
    if not is_exist:
        print("遍历了一边，都没有找到...")
        raise NoSuchElementException("select not contains option={}".format(value))


# 判断页面中是否存在指定的文本内容
def exist_text(driver, text):
    try:
        xpath = "//*[contains(text(), '{}')]".format(text)
        ele = driver.find_element_by_xpath(xpath)
        return ele is not None
    except Exception as e:
        print("current page is not contains text={}".format(text))
        return False


class DriverUtil:
    _mp_driver = None  # 自媒体
    _mis_driver = None  # 后台管理系统
    _app_driver = None  # APP

    _mp_auto_quit = True
    _mis_auto_quit = True
    _app_auto_quit = True

    # 自媒体
    # 获取驱动对象
    @classmethod
    def get_mp_driver(cls):
        if cls._mp_driver is None:
            cls._mp_driver = selenium.webdriver.Chrome()
            cls._mp_driver.maximize_window()
            cls._mp_driver.implicitly_wait(30)
            cls._mp_driver.get("http://ttmp.research.itcast.cn/")
        return cls._mp_driver

    # 关闭驱动对象
    @classmethod
    def quit_mp_driver(cls):
        if cls._mp_driver and cls._mp_auto_quit:
            cls._mp_driver.quit()
            cls._mp_driver = None

    # 设置驱动关闭的开关
    @classmethod
    def set_mp_auto_quit(cls, auto_quit):
        cls._mp_auto_quit = auto_quit

    # 后台管理系统
    # 获取驱动对象
    @classmethod
    def get_mis_driver(cls):
        if cls._mis_driver is None:
            cls._mis_driver = selenium.webdriver.Chrome()
            cls._mis_driver.maximize_window()
            cls._mis_driver.implicitly_wait(30)
            cls._mis_driver.get("http://ttmis.research.itcast.cn/")
        return cls._mis_driver

    # 关闭驱动对象
    @classmethod
    def quit_mis_driver(cls):
        if cls._mis_driver and cls._mis_auto_quit:
            cls._mis_driver.quit()
            cls._mis_driver = None

    # 设置驱动关闭的开关
    @classmethod
    def set_mis_auto_quit(cls, auto_quit):
        cls._mis_auto_quit = auto_quit

    # APP
    # 获取驱动对象
    @classmethod
    def get_app_driver(cls):
        if cls._app_driver is None:
            cap = {
                "platformName": "Android",
                "deviceName": "emulator",
                "appPackage": "com.itcast.toutiaoApp",
                "appActivity": ".MainActivity",
                "noReset": True,
            }
            cls._app_driver = appium.webdriver.Remote("http://127.0.0.1:4723/wd/hub", cap)
            cls._app_driver.implicitly_wait(10)
        return cls._app_driver

    # 关闭驱动对象
    @classmethod
    def quit_app_driver(cls):
        if cls._app_auto_quit and cls._app_driver:
            cls._app_driver.quit()
            cls._app_driver = None

    # 设置驱动关闭的开关
    @classmethod
    def set_app_auto_quit(cls, auto_quit):
        cls._app_auto_quit = auto_quit
