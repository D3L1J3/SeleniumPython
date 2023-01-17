import time
import unittest

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


# This code is a test suite for a Google search page, it includes three test cases:
# Test1 - test_page_title: It navigates to the Google homepage and verifies that the title of
# the page is "Google".
#
# Test-2 test_search_for_selenium: It navigates to the Google homepage,
# clicks on the accept button, searches for Selenium in the search bar, waits for 1 second,
# verifies that the title of the page includes "Selenium",
# and verifies that the Google logo is displayed.
#
# Test-3 test_click_on_images_link: It navigates to the Google homepage,
# clicks on the accept button, clicks on the Images link,
# and verifies that the current URL is "https://www.google.se/imghp?hl=sv&ogbl"

class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def test_page_title(self):
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)

    def test_search_for_selenium(self):
        self.browser.get("https://www.google.com")
        acceptButton = self.browser.find_element(By.CSS_SELECTOR, "button#L2AGLb")
        acceptButton.click()
        search_field = self.browser.find_element(By.NAME, "q")
        search_field.send_keys("Selenium", Keys.RETURN)
        time.sleep(1)
        self.assertIn("Selenium", self.browser.title)
        logo_element = self.browser.find_element(By.ID, "logo")
        self.assertTrue(logo_element.is_displayed())

    def test_click_on_images_link(self):
        self.browser.get("https://www.google.com")
        acceptButton = self.browser.find_element(By.CSS_SELECTOR, "button#L2AGLb")
        acceptButton.click()
        images_link = self.browser.find_element(By.CSS_SELECTOR, "a.gb_m[data-pid='2']")
        images_link.click()
        self.assertEqual(self.browser.current_url, "https://www.google.se/imghp?hl=sv&ogbl")
