# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest

class foothilldir(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://deanza.edu/directory/dir-az.html"
        self.verificationErrors = []

    def do_work(self, driver, link_text, title_word):

        driver.get(self.base_url)
        driver.find_element_by_link_text(link_text).click()
        try: self.assertRegexpMatches(driver.title, title_word)
        except AssertionError as e: self.verificationErrors.append(str(e))

    def test_foothill_dir(self):
        
        driver = self.driver

        self.do_work(driver, "Kirsch Center for Environmental Studies", r"Kirsch")
        self.do_work(driver, "Korean Department", r"Korean")
        self.do_work(driver, "Language Arts", r"Language")
        self.do_work(driver, "Learning in Communities", r"Learning")
        self.do_work(driver, "Library/De Hart Learning Center", r"Library")
        self.do_work(driver, "Library West Computer Lab", r"Computer")
        self.do_work(driver, "Listening and Speaking Center", r"Listening")
        self.do_work(driver, "Learning Resources Divisio", r"Resources")

        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()