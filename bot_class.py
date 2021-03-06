from selenium import webdriver
from time import sleep
import urllib
import urllib.request
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
class RedditBot():
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        chrome_options.add_experimental_option("prefs",prefs)
        self.browser = webdriver.Chrome(executable_path='/Users/glebsvarcer/Documents/instabot/chromedriver',chrome_options=chrome_options)
    def get_from_reddit(self,subreddit):
        self.browser.get('https://reddit.com/r/'+str(subreddit))
        sleep(2)
        op_user = self.browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div/div[2]/div[3]/div[1]/div[4]/div[2]/div/div/div[2]/div[1]/div/div[1]/div/a').text
        thought = self.browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div/div[2]/div[3]/div[1]/div[4]/div[2]/div/div/div[2]/div[2]/div[1]/a/div/h3').text
        upvotes = self.browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div/div[2]/div[3]/div[1]/div[4]/div[2]/div/div/div[1]/div/div').text
        link = self.browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div/div[2]/div[3]/div[1]/div[4]/div[2]/div/div/div[2]/div[2]/div[1]/a').get_attribute('href')
        return op_user, thought, upvotes, link
        sleep(1)
    def translate(self,message):
        self.browser.get('https://translate.google.com/#view=home&op=translate&sl=en&tl=ru')
        sleep(5)
        self.browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div/div/div[1]/textarea').send_keys(message)
        sleep(3)
        translated = self.browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div/span[1]/span').text
        return translated
        sleep(1)
    def post_to_vk(self,username,password,message):
        self.browser.get('https://vk.com')
        sleep(5)
        self.browser.find_element_by_xpath('/html/body/div[9]/div/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div[1]/form/input[7]').send_keys(username)
        self.browser.find_element_by_xpath('/html/body/div[9]/div/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div[1]/form/input[8]').send_keys(password)
        self.browser.find_element_by_xpath('/html/body/div[9]/div/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div[1]/form/button').click()
        sleep(5)
        self.browser.find_element_by_xpath('/html/body/div[11]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]').click()
        sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[11]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div/div/div[1]/div[1]/div[3]/div[4]').send_keys(message)
        sleep(5)
        self.browser.find_element_by_xpath('/html/body/div[11]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div[4]/div[5]/div[1]/div').click
        #self.browser.find_element_by_xpath('/html/body/div[11]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div/div/div[1]/div[1]/div[6]/div[1]/button').click()
        sleep(1)