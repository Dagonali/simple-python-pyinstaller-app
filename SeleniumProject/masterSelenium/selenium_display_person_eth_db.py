"""

Ali Da Silva Ouederni
Sept. 2019

"""
import os
import sys
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = 'http://seismo.ethz.ch/about-us/all-employees/ali-da-silva/index.html'

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver',
                          chrome_options=chrome_options)

# Opens Chrome with given url
driver.get(url)

# To get the xPath; Inspect element you want the xPath from -> right click it
# -> Copy -> Copy xPath

mail = driver.find_element_by_xpath(
        '//*[@id="page-complete"]/div[2]/div/div'
        '/div[2]/div[1]/div/div/div/div/div[8]')

phone_number = driver.find_element_by_xpath(
            '//*[@id="page-complete"]/div[2]/div/div'
            '/div[2]/div[1]/div/div/div/div/div[7]')


class SeleniumTests(unittest.TestCase):

    def test_get_mail(self):
        """
        Testing if Seismo Website gives back the mail of
        searched person
        """
        try:
            if mail:
                print('Mail: ' + mail.text)
                return True
            else:
                print('No Mail found')
                return False
        except Exception as exception:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            exc_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, exc_name, exc_tb.tb_lineno)
            print(exception)

    def test_get_phone_number(self):
        """
        Testing if Seismo Website gives back the phone number of
        searched person
        """
        try:
            if phone_number:
                print('Phone number: ' + phone_number.text)
                return True
            else:
                print('No phone number found!')
                return False
        except Exception as exception:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            exc_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, exc_name, exc_tb.tb_lineno)
            print(exception)


if __name__ == '__main__':
    unittest.main()
