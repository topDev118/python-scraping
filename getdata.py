import requests
from bs4 import BeautifulSoup
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://www.freelancer.com/u/wang109')

soup = BeautifulSoup(browser.page_source, 'html.parser')
print(soup.find('h1').text)