from selenium import webdriver

browser = webdriver.Chrome()

host = 'http://localhost:8000'

browser.get(host)

assert 'Django' in browser.title