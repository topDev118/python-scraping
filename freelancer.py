from selenium import webdriver as wd
import random
import string
import time


driver = wd.Firefox()
#main URL setting
main_url = ''



def random_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
fake_email = random_generator(8, "6793YUIOXetGD") + '@hotmail.com'
fakepassword = random_generator(16, "DGtewa#6793YUIOXeqwetewttGD!!4#$")

#go to URL

driver.get(main_url)

#find searchbox and enter the keyword
#search box id = twotabsearchtextbox
driver.find_element_by_id('new-email').send_keys(fake_email)
driver.find_element_by_id('new-password').send_keys(fakepassword)


#wait a little while the page fully loading
time.sleep(2)

#sign up button click
driver.find_element_by_css_selector('#signup_btn').click()

#username generating
username = random_generator(8, "abcdefghijklmnopqrstuvwxyz")
#input username
driver.find_element_by_id('new-username').send_keys(username)
#delay
time.sleep(3)
#click next button
driver.find_element_by_css_selector('.ModalLoginSignup-signupUsernameInput-submitBtn').click()
#click I want to hire
driver.find_element_by_css_selector('[alt="Hire Image"]').click()

#delay
time.sleep(20)
#click tutorial skip link
driver.find_element_by_css_selector('.PageEmployerOnboarding-stepContainer-skip').click()

#title and description define
title = 'Build me a website'
description = 'I need an honest man. Already domain is purchased and hosted it. Send me the resume. projectonline003 @ hotmail.com      Please contact me for more details.'


#input title
driver.find_element_by_css_selector('.large-input').send_keys(title)
#input description
driver.find_element_by_id('project-description').send_keys(description)

time.sleep(1)

# #add the skill list
# driver.find_element_by_css_selector('.new-skill-suggestion-link').click()
#delay
time.sleep(2)
#click next button
driver.find_element_by_css_selector('.PagePostProject-submit-btn').click()
time.sleep(1)
#click next button
driver.find_element_by_css_selector('.PagePostProject-submit-btn').click()
#delay
time.sleep(3)
#click Post a Project
driver.find_element_by_xpath('/html/body/div[1]/main/section/fl-project-create/div/fl-wizard-form/div/form/ol/li[4]/fl-contest-upsell/div/fieldset/nav/ul/li[1]/label').click()
#delay
time.sleep(2)
#click fixed project
driver.find_element_by_xpath('/html/body/div[1]/main/section/fl-project-create/div/fl-wizard-form/div/form/ol/li[5]/fl-budget-selector/div/fieldset/span/nav/ul/li[1]/label/div/div').click()
#delay
time.sleep(2)
#click next button
driver.find_element_by_css_selector('.PagePostProject-submit-btn').click()
#delay
time.sleep(2)
#click standard FREE project
driver.find_element_by_xpath('/html/body/div[1]/main/section/fl-project-create/div/fl-wizard-form/div/form/ol/li[7]/fl-post-project-upgrades/div[1]/fieldset/nav/ul/li[1]/label/div/div[1]').click()

driver.find_element_by_css_selector('.PagePostProject-submit-btn').click()





