from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes to check out it's homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title mentions to-do lists:
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away

        # She types "Buy Peacock feathers", into the text box.

        # When she hits 'enter', the page updatesm and now the page lists:
        # "1: Buy Peacock feathers" as an item in the to-do list

        # There is still a text box inviting her to add mote items to the list as before.
        # She enters "Use Peacock feathers to make a fly"

        # The page updates again, and now both items appear on her list.

        # Edith wonders if the site will remember her list. She sees that the site generated a unique URL for her
        # and there is some text to that effect.

        # She visits that URL  - and her to-do list is still there!

        # Satisfied she turns off her computer and she goes back to sleep.
if __name__ == '__main__':
    unittest.main(warnings='ignore')