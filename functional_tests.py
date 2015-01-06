from selenium import webdriver

broswer = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title
