import sys, pytest
from time import sleep

sys.path.append("E:\python\Po_2")

from Base import Get_data, init_driver
from Page.page import Page


def data():
    data = Get_data.get_data("Search_Data").get("Data")
    # 只取出有用的数据，而不取表头
    # 将取出来的字典数据，转入列表中
    data_list = []
    for i in data.keys():
        data_list.append((i, data.get(i).get("test")))
    return data_list

def data2(key):
    #根据最上层字典的键  获取第二层对应的测试用例数据  ：｛search_001：{test:xxx,name:xxx}, search_002：{test:xxxx,name:xxxx}｝
    data = Get_data.get_data("Search_Data")[key]
    # 取出多个字典转入 一个列表中，在方法使用参数的时候，只要用 每个字典的键名 就可以获取对应值
    #[{test:xxx,name:xxx},{test:xxxx,name:xxxx}]  如这里有2个字典，即会执行2次测试，每次
    #测试分别传入一个字典，之后再方法内使用这个字典的键 获取值
    data_list = []
    for i in data.values():
        data_list.append(i)
    return data_list

class Test_a:
    def setup_class(self):
        self.driver = init_driver.init_driver()
        self.search_obj = Page(self.driver).return_search_obj()

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.parametrize("test_num,test", data())
    def test_001(self, test_num, test):
        self.search_obj.search_botton()

        self.search_obj.search_input(test)
        sleep(2)
        assert self.driver.get_screenshot_as_file("./screen/%s.png" % test_num)

