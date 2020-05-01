from Base.Base import Base
import Page


class Search(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def search_botton(self):
        self.click_element(Page.search_btn)

    def search_input(self, text):
        self.input_element(Page.search_input, text)

    def search_back(self):
        self.click_element(Page.search_back)
