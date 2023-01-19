import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

# This code is a test suite for a form on a website using
# Selenium with the Firefox webdriver. The test navigates to a website and
# fills out the form with specific test data, submits the form,
# and asserts that the success message is displayed on the page
# after the form is submitted. The setUp method navigates to the website,
# and the tearDown method closes the webdriver.
class FormTestSuite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://rahulshettyacademy.com/angularpractice/")

    def test_form_submission(self):
        # Find and fill out the name field
        name_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='name']")
        name_field.send_keys("John Smith")

        # Find and fill out the email field
        email_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='email']")
        email_field.send_keys("johnsmith@example.com")

        # Find and fill out the password field
        password_field = self.driver.find_element(By.CSS_SELECTOR, "input[type='password']")
        password_field.send_keys("password123")

        gender_element = self.driver.find_element(By.ID, "exampleFormControlSelect1")
        male_option = gender_element.find_element(By.XPATH, "//option[text()='Female']")
        male_option.click()

        employed_option = self.driver.find_element(By.XPATH, "//input[@value='option2']")
        employed_option.click()

        date_of_birth_field = self.driver.find_element(By.NAME, "bday")
        date_of_birth_field.send_keys("1990-01-01")

        submit_button = self.driver.find_element(By.CSS_SELECTOR, "input.btn.btn-success")
        submit_button.click()
        success_message = self.driver.find_element(By.CSS_SELECTOR, "div.alert.alert-success.alert-dismissible")
        self.assertTrue(success_message.is_displayed())

    def tearDown(self):
        if self.driver:
            self.driver.quit()




