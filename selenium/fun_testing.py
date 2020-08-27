import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox(executable_path='driver/geckodriver')

    def test_blogger_login_page(self):
        driver=self.driver
        driver.get('https://www.google.com')

    def tearDown(self):
        self.driver.quit()


if __name__=='__main__':
    unittest.main()
