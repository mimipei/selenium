from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
url = "http://sahitest.com/demo/index.htm"
driver.get(url)
driver.maximize_window()