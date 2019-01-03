from locators import MainPageLocators, SearchResultsPageLocators, HabrPageLocators, SandBoxPageLocators, SecondSandBoxPageLocators, ArticlePageLocators
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


class BasePage(object):
  
    def __init__(self, driver):
        self.driver = driver

    def is_exist(self, by, path):
        try:
            self.driver.find_element( by, path)
            return True
        except Exception:
            return False
            pass


class MainPage(BasePage):

    def search_custom_data(self, text):
        search_field = self.driver.find_element(*MainPageLocators.SEARCH_FIELD)
        search_field.send_keys(text, Keys.ENTER)


class SearchResultsPage(BasePage):

    def is_results_found(self):
        return "ничего не найдено" not in self.driver.page_source

    def go_to_first_related_page(self, text):
 
        for res in self.driver.find_elements(*SearchResultsPageLocators.SEARCH_RESULTS):
            tmp = res.get_attribute("href")
            if text in tmp:
                res.click()
                return

class HabrPage(BasePage):

    def go_to_sandbox(self):
        assert self.is_exist(*HabrPageLocators.SANDBOX), "Sandbox element is not found"
        self.driver.find_element(*HabrPageLocators.SANDBOX).click()

class SandBoxPage(BasePage):
    def go_to_second(self):
        assert self.is_exist(*SandBoxPageLocators.SANDBOX_SCND), "Second sandbox element is not found"
        self.driver.find_element(*SandBoxPageLocators.SANDBOX_SCND).click()
        pass

class SecondSandBoxPage(BasePage):
    def first_article_element_present(self):
        return self.is_exist(*SecondSandBoxPageLocators.FIRST_ARTICLE)
        

    def get_first_article_header(self):
        return self.driver.find_element(*SecondSandBoxPageLocators.FIRST_ARTICLE).text
        

    def go_to_first_article(self):
        self.driver.find_element(*SecondSandBoxPageLocators.FIRST_ARTICLE).click()
        pass
        

class ArticlePage(BasePage):

    def is_header_same(self, header):
        return header in self.driver.find_element(*ArticlePageLocators.HEADER).text