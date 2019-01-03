from selenium.webdriver.common.by import By

class MainPageLocators(object):
    SEARCH_FIELD = (By.CSS_SELECTOR,'input.gLFyf.gsfi')
    

class SearchResultsPageLocators(object):
   SEARCH_RESULTS = (By.XPATH,"//div[@class = 'rc']/div/a")

class HabrPageLocators(object):
    SANDBOX = (By.XPATH,"//a[@href = 'https://habr.com/sandbox/']")

class SandBoxPageLocators(object):
    SANDBOX_SCND = (By.XPATH,"//a[@href = '/sandbox/page2/']")

class SecondSandBoxPageLocators(object):
    FIRST_ARTICLE = (By.XPATH,"//h2[@class = 'post__title']//child::a")

class ArticlePageLocators(object):
    HEADER = (By.XPATH,"//h1[@class = 'post__title']//child::span")