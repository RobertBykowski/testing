from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome("C:/atestfiles/chromedriver.exe")
# driver = webdriver.Chrome(executable_path=r'C:\testfiles/chromedriver.exe')
driver.get("http://google.com")
# title = driver.title
# print(title)
search = driver.find_element_by_name("q")
search.send_keys("Robert Bykowski", Keys.RETURNE)
