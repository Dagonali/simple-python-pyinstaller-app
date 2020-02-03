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
# url2 = 'file:///home/alid/Projects/SeleniumProject/masterSelenium/test.html'
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
tel = driver.find_element_by_xpath(
    '//*[@id="page-complete"]/div[2]/div/div'
    '/div[2]/div[1]/div/div/div/div/div[7]')
mail = driver.find_element_by_xpath(
    '//*[@id="page-complete"]/div[2]/div/div'
    '/div[2]/div[1]/div/div/div/div/div[8]')


class SeleniumTest(unittest.TestCase):

    def test_get_mail(mail):
        try:
            if mail:
                print('Mail True: ' + mail.text)
                return True
            else:
                print('Mail False')
                return False
        except Exception as exception:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            exc_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, exc_name, exc_tb.tb_lineno)
            print(exception)

    def test_get_tel(tel):
        try:
            if tel:
                print('Telephone True: ' + tel.text)
                return True
            else:
                print('Tel False')
                return False
        except Exception as exception:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            exc_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, exc_name, exc_tb.tb_lineno)
            print(exception)


if __name__ == '__main__':
    unittest.main()
