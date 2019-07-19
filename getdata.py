import requests
from bs4 import BeautifulSoup
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://www.freelancer.com/projects/html/Web-Page-Design-20409303/details')

soup = BeautifulSoup(browser.page_source, 'html.parser')
print(soup.find('div').text)