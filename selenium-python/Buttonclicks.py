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
buttonclicks=driver.find_element(By.XPATH, "//*[@class='section-title']/h1[contains(text() ,'BUTTON CLICKS')]")
buttonclicks.click()




parentwindow=driver.current_window_handle
child=driver.window_handles[1]
driver.switch_to.window(child)

clickme1 = driver.find_element(By.XPATH, "//*[@id='button1']")
clickme1.click()

driver.close()
#time.sleep(3)




