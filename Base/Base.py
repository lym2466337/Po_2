from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait



class Base:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, loc, timeout=10, fre=0.5):
        by=loc[0]
        #如果 是xpath的方式，通过调用方法拼接xpath路径，而find_elemnt的 loc[1]格式 值需要  "text,设置" 或者一个列表包含多个字符串
        path=loc[1]  #"text,设置"
        if by==By.XPATH:
            path = self.make_xpath_with_feature(path)  # 转换成语句
        #若是其他方式也能正常查找，xpath方式拼接后的字符也能正常传入 查找
        return WebDriverWait(self.driver, timeout, fre) \
            .until(lambda x: x.find_element(by,path))

    def click_element(self, loc):
        self.find_element(loc).click()

    def input_element(self, loc, text):
        ele= self.find_element(loc)
        ele.clear()
        ele.send_keys(text)


    def make_xpath_with_feature(self, loc):
        feature_start = "//*["
        feature_end = "]"
        feature = ""

        if isinstance(loc, str):
            # 如果是正常的xpath字符串,直接返回输入的语句，无需拼接
            if loc.startswith("//"):
                return loc

            # loc str
            feature = self.make_xpath_with_unit_feature(loc)
        else:
            # loc 列表
            # 无论多条件还是单条件  都以and结尾，最后再去除最后一个and，且and后面加一个空格，避免and后面的类似contains无法被识别
            for i in loc:
                feature += self.make_xpath_with_unit_feature(i)

        feature = feature.rstrip("and ")

        loc = feature_start + feature + feature_end

        return loc

    def make_xpath_with_unit_feature(self, loc):
        """
        拼接xpath中间的部分
        :param loc:
        :return:
        """
        key_index = 0
        value_index = 1
        option_index = 2

        args = loc.split(",")
        feature = ""

        if len(args) == 2:
            feature = "contains(@" + args[key_index] + ",'" + args[value_index] + "')" + "and "
        elif len(args) == 3:
            if args[option_index] == "1":
                feature = "@" + args[key_index] + "='" + args[value_index] + "'" + "and "
            elif args[option_index] == "0":
                feature = "contains(@" + args[key_index] + ",'" + args[value_index] + "')" + "and "

        return feature

