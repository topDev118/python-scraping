from selenium import webdriver as wd
driver = wd.Firefox()
#main URL setting
main_url = 'https://www.amazon.com/'
#search keyword
keyword = 'hand bag'
#go to URL
driver.get(main_url)

#find searchbox and enter the keyword
#search box id = twotabsearchtextbox
driver.find_element_by_id('twotabsearchtextbox').send_keys(keyword)

#search button click

driver.find_element_by_css_selector('.nav-search-submit').click()

#wait a little while the page fully loading
