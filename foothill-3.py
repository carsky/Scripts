# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest

class foothilldir(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://deanza.edu/directory/dir-az.html"
        self.verificationErrors = []

    def test_sauce_labs_headers(self):
        
        driver = self.driver

        driver.get(self.base_url)
        driver.find_element_by_link_text("Kirsch Center for Environmental Studies").click()
        try: self.assertRegexpMatches(driver.title, r"Kirsch")
        except AssertionError as e: self.verificationErrors.append(str(e))

        driver.get(self.base_url)
        driver.find_element_by_link_text("Korean Department").click()
        try: self.assertRegexpMatches(driver.title, r"Korean")
        except AssertionError as e: self.verificationErrors.append(str(e))

        driver.get(self.base_url)
        driver.find_element_by_link_text("Language Arts").click()
        try: self.assertRegexpMatches(driver.title, r"Language")
        except AssertionError as e: self.verificationErrors.append(str(e))

        driver.get(self.base_url)
        driver.find_element_by_link_text("Learning in Communities").click()
        try: self.assertRegexpMatches(driver.title, r"Learning")
        except AssertionError as e: self.verificationErrors.append(str(e))
        
        driver.get(self.base_url)
        driver.find_element_by_link_text("Library/De Hart Learning Center").click()
        try: self.assertRegexpMatches(driver.title, r"Library")
        except AssertionError as e: self.verificationErrors.append(str(e))
        
        driver.get(self.base_url)
        driver.find_element_by_link_text("Library West Computer Lab").click()
        try: self.assertRegexpMatches(driver.title, r"Computer")
        except AssertionError as e: self.verificationErrors.append(str(e))
        
        driver.get(self.base_url)
        driver.find_element_by_link_text("Listening and Speaking Center").click()
        try: self.assertRegexpMatches(driver.title, r"Listening")
        except AssertionError as e: self.verificationErrors.append(str(e))
        
        driver.get(self.base_url)
        driver.find_element_by_link_text("Learning Resources Divisio").click()
       
        try: 
            self.assertRegexpMatches(driver.title, r"Resources")
        except AssertionError as e: 
            self.verificationErrors.append(str(e))
        
       
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()