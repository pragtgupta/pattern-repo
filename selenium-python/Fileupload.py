import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

service = Service(executable_path="../drivers/chromedriver")
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://webdriveruniversity.com/")

wait = WebDriverWait(driver, 6)
fileupload=driver.find_element(By.XPATH, "//*[@class='section-title']/h1[contains(text() ,'FILE UPLOAD')]")
fileupload.click()

parentwindow = driver.current_window_handle
child = driver.window_handles[1]
driver.switch_to.window(child)

#/Users/pkiranjikumar/Downloads/Firefox 100.0.2.dmg
driver.find_element(By.CSS_SELECTOR,"#myFile").send_keys("/Users/pragtgupta/Downloads/pycharm-community-2022.1.1.dmg")
time.sleep(3)




