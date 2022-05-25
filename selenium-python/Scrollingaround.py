import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys



service = Service(executable_path="../drivers/chromedriver")
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://webdriveruniversity.com/")

wait = WebDriverWait(driver, 6)
button_clicks = driver.find_element(By.XPATH, "//*[@class='section-title']/h1[contains(text() ,'SCROLLING AROUND')]")
button_clicks.click()


parentwindow=driver.current_window_handle
child=driver.window_handles[1]
driver.switch_to.window(child)

#zone1=driver.find_elements(By.XPATH,"(//*[@class='col-lg-12']/div/h1)[1]")
zone1=driver.find_element(By.XPATH,"//*[@id='zone1']/h1")
action=ActionChains(driver)
action.move_to_element(zone1).perform()
zone1=driver.find_element(By.XPATH,"//*[@id='zone1']")
print(zone1.text)
assert zone1.text =="Well done for scrolling to me!"

zone2=driver.find_element(By.XPATH,"//*[@id='zone2-entries']")
action.move_to_element(zone2).perform()
zone2=driver.find_element(By.XPATH,"//*[@id='zone2-entries']")
print(zone2.text)
assert zone2.text =="1 Entries"