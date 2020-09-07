import unittest
from selenium import webdriver



class Test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("--window-size=1920,1080")
        self.driver=webdriver.Chrome(executable_path='driver/chromedriver_linux64/chromedriver',options=chrome_options)



    def test_blogger_launch_and_redirect_to_login(self):
        driver=self.driver
        driver.get('https://flask-app-k264k77ofq-as.a.run.app/') #launching the blogger application
        element=driver.find_element_by_xpath("//a[contains(@href,'login')]")
        element.click() # clicking the login button on home page


    def test_blogger_user_to_login(self):
        driver=self.driver
        user=driver.find_element_by_name('email')
        password=driver.find_element_by_id('pass')
        user.send_keys('prasad@gmail.com')
        password.send_keys('password')
        signin=driver.find_element_by_xpath("//button[contains(@type,'submit')]")
        signin.click()
        element=driver.find_element_by_xpath("//a[@href='/']")
        text=element.text
        self.assertEqual(text.lower(),"welcome prasad")


    @classmethod
    def tearDownClass(self):
        self.driver.quit()


if __name__=='__main__':
    unittest.main()
