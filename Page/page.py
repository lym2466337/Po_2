from Page.search import Search
class Page:
    def __init__(self,driver):
        self.driver =driver

    def return_search_obj(self):
        return Search(self.driver)
