"""

Ali Da Silva Ouederni
Sept. 2019

"""
import os
import sys
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

url_en = 'http://seismo.ethz.ch/en/home/'
url_de = 'http://seismo.ethz.ch/de/home/'
# url2 = 'file:///home/alid/Projects/SeleniumProject/masterSelenium/test.html'

driver = webdriver.Chrome('/usr/local/share/chromedriver')
second_driver = webdriver.Chrome('/usr/local/share/chromedriver')
# Opens Chrome with given url
driver.get(url_en)
second_driver.get(url_de)
# To get the xPath; Inspect element you want the xPath from -> right click it
# -> Copy -> Copy xPath
# tel = driver.find_element_by_xpath(
#     '//*[@id="page-complete"]/div[2]/div/div'
#     '/div[2]/div[1]/div/div/div/div/div[7]')
# mail = driver.find_element_by_xpath(
#     '//*[@id="page-complete"]/div[2]/div/div'
#     '/div[2]/div[1]/div/div/div/div/div[8]')
search_button_en = driver.find_element_by_xpath(
    '//*[@id="search_block"]')
search_button_de = second_driver.find_element_by_xpath(
    '//*[@id="search_block"]')
search_en = driver.find_element_by_xpath(
    '//*[@id="searchWidgetAutoCompleteHeader"]')
search_de = second_driver.find_element_by_xpath(
    '//*[@id="searchWidgetAutoCompleteHeader"]')
action_en = ActionChains(driver)
action_de = ActionChains(second_driver)


class SeleniumTest(unittest.TestCase):

    #def get_mail(self):
    #    try:
    #        if self:
    #            print('Mail True: ' + self.text)
    #            return True
    #        else:
    #            print('Mail False')
    #            return False
    #    except Exception as exception:
    #        exc_type, exc_obj, exc_tb = sys.exc_info()
    #        exc_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    #        print(exc_type, exc_name, exc_tb.tb_lineno)
    #        print(exception)

    #def get_tel(self):
    #    try:
    #        if self:
    #            print('Telephone True: ' + self.text)
    #            return True
    #        else:
    #            print('Tel False')
    #            return False
    #    except Exception as exception:
    #        exc_type, exc_obj, exc_tb = sys.exc_info()
    #        exc_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    #        print(exc_type, exc_name, exc_tb.tb_lineno)
    #        print(exception)
    def test_get_search_en(search):
        try:
            if search:
                action_en.click(search_button_en)
                action_en.click(search_en)
                action_en.pause(1)
                action_en.send_keys("valais")
                action_en.pause(3)
                action_en.send_keys(Keys.ENTER)
                action_en.pause(3)
                action_en.perform()
                show_url_en = driver.current_url
                if show_url_en != url_en:
                    en_second_driver = driver
                    action_en_sec = ActionChains(en_second_driver)
                    searching_en = en_second_driver.find_element_by_xpath(
                        '/html/body/div[1]/div/div[2]/div/div/div/div/div['
                        '2]/div/div/div[2]/div[2]/div[5]/div/div[1]')
                    action_en_sec.click(searching_en)
                    action_en_sec.perform()
                    headline_en = en_second_driver.find_element_by_xpath(
                        '//*[@id="72dd5452-05e7-11e5-aa78-00ff00000250-column1'
                        '-5e7c099a-6f76-11e6-94af-00ff00000250"]/div[1]')
                    print("Headline_EN: " + headline_en.text)
                    print("URL_EN: " + show_url_en)
            else:
                print('Search False')
                return False
        except Exception as exception:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            exc_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, exc_name, exc_tb.tb_lineno)
            print(exception)

    def test_get_search_de(search):
        try:
            if search:
                action_de.click(search_button_de)
                action_de.click(search_de)
                action_de.pause(1)
                action_de.send_keys("wallis")
                action_de.pause(3)
                action_de.send_keys(Keys.ENTER)
                action_de.pause(3)
                action_de.perform()
                show_url_de = second_driver.current_url
                if show_url_de != url_de:
                    de_second_driver = second_driver
                    action_de_sec = ActionChains(de_second_driver)
                    searching_de = de_second_driver.find_element_by_xpath(
                        '/html/body/div[1]/div/div[2]/div/div/div/div/div['
                        '2]/div/div/div[2]/div[2]/div[5]/div/div[1]')
                    action_de_sec.click(searching_de)
                    action_de_sec.perform()
                    headline_de = de_second_driver.find_element_by_xpath(
                        '//*[@id="72dd5452-05e7-11e5-aa78-00ff00000250-column1'
                        '-5e7c099a-6f76-11e6-94af-00ff00000250"]/div[1]')
                    print("Headline_DE: " + headline_de.text)
                    print("URL_DE: " + show_url_de)
            else:
                print('Search False')
                return False
        except Exception as exception:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            exc_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, exc_name, exc_tb.tb_lineno)
            print(exception)


if __name__ == '__main__':
    unittest.main()
