from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from sys import stdin

driver = webdriver.Chrome("." + "\\chromedriver.exe")
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()

# equivalente ao console.readline()
stdin.readline()

elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
# driver.close()