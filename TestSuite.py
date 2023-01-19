import time
import unittest
from os import name

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


# This code is a test suite for a Google search page, it includes four test cases:
# Test1 - test_page_title: It navigates to the Google homepage and verifies that the title of
# the page is "Google".
#
# Test-2 test_search_for_selenium: It navigates to the Google homepage,
# clicks on the accept button, searches for Selenium in the search bar, waits for 1 second,
# verifies that the title of the page includes "Selenium",
# and verifies that the Google logo is displayed.
#
# Test-3 test_search_for_images: Navigates to the Google Images homepage,
# clicks the accept button, searches for "Selenium",
# and then checks that there are more than 0 images displayed on the page.

# Test-4 test_click_on_sign_in_button: Navigates to the google homepage,
# clicks on the accept button, clicks on the sign in link,
# and then asserts that the current URL contains "accounts.google.com/v3/signin/identifier".

# setUp method opens a Firefox browser and navigates to the Google homepage
# The tearDown method closes the browser after all tests are run.
# The if statement at the end of the code allows the test suite to be run as the main program.

class GoogleTestCase(unittest.TestCase):

    browser = None
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get("https://www.google.com")
        options = webdriver.FirefoxOptions()
        options.add_argument('--disable-popup-blocking')

    def test_page_title(self):
        self.assertIn('Google', self.browser.title)

    def test_search_for_selenium(self):
        acceptButton = self.browser.find_element(By.CSS_SELECTOR, "button#L2AGLb")
        acceptButton.click()
        search_field = self.browser.find_element(By.NAME, "q")
        search_field.send_keys("Selenium", Keys.RETURN)
        time.sleep(1)
        self.assertIn("Selenium", self.browser.title)
        logo_element = self.browser.find_element(By.ID, "logo")
        self.assertTrue(logo_element.is_displayed())

    def test_search_for_images(self):
        self.browser.get("https://www.google.com/imghp")
        acceptButton = self.browser.find_element(By.CSS_SELECTOR, "button#L2AGLb")
        acceptButton.click()
        search_field = self.browser.find_element(By.NAME, "q")
        search_field.send_keys("Selenium", Keys.RETURN)
        time.sleep(1)
        images_list = self.browser.find_elements(By.CSS_SELECTOR, "img.rg_i")
        self.assertTrue(len(images_list) > 0)

    def test_click_on_sign_in_button(self):
        acceptButton = self.browser.find_element(By.CSS_SELECTOR, "button#L2AGLb")
        acceptButton.click()
        sign_in_link = self.browser.find_element(By.CSS_SELECTOR, "a.gb_ha.gb_ia.gb_ee.gb_ed")
        sign_in_link.click()
        self.assertIn("accounts.google.com/v3/signin/identifier", self.browser.current_url)

    def tearDown(self):
        if self.browser:
            self.browser.quit()

if name == 'main':
    unittest.main()


