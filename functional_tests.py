from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # She types "Buy Peacock feathers", into the text box.
        inputbox.send_keys('Buy peacock feathers')

        # When she hits 'enter', the page updatesm and now the page lists:
        # "1: Buy Peacock feathers" as an item in the to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == '1: Buy peacock feathers' for row in rows),
                        "New to-do item did not appear in table")
        # There is still a text box inviting her to add mote items to the list as before.
        # She enters "Use Peacock feathers to make a fly"
        self.fail('Finish the test!')

        # The page updates again, and now both items appear on her list.

        # Edith wonders if the site will remember her list. She sees that the site generated a unique URL for her
        # and there is some text to that effect.

        # She visits that URL  - and her to-do list is still there!

        # Satisfied she turns off her computer and she goes back to sleep.


if __name__ == '__main__':
    unittest.main(warnings='ignore')
