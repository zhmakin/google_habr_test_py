import unittest
from selenium import webdriver
import pages

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe")
        self.driver.get("https://www.google.com")

    def test_search_in_python_org(self):

        search_text = "habrahabr"

        main_page = pages.MainPage(self.driver)

        main_page.search_custom_data(search_text)
        
        search_results_page = pages.SearchResultsPage(self.driver)
        assert search_results_page.is_results_found()
        search_results_page.go_to_first_related_page(search_text)

        pages.HabrPage(self.driver).go_to_sandbox()

        pages.SandBoxPage(self.driver).go_to_second()

        second_sandbox_page = pages.SecondSandBoxPage(self.driver)
        assert second_sandbox_page.first_article_element_present(), "Second sandbox page element is not found"
        article_header = second_sandbox_page.get_first_article_header()

        second_sandbox_page.go_to_first_article()

        article_page = pages.ArticlePage(self.driver)
        assert article_page.is_header_same(article_header), "Article header does not match"

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()