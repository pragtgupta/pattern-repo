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
button_clicks = driver.find_element(By.XPATH, "//*[@class='section-title']/h1[contains(text() ,'ACTIONS')]")
button_clicks.click()

parentwindow = driver.current_window_handle
child = driver.window_handles[1]
driver.switch_to.window(child)

drag = driver.find_element(By.XPATH, "//*[@id='draggable']")
drop = driver.find_element(By.XPATH, "//*[@id='droppable']")
action = ActionChains(driver)
action.drag_and_drop(drag, drop).perform()
droptext = driver.find_element(By.XPATH, "//*[@id='droppable']/p/b")
assert droptext.text == "Dropped!"

doubleclick = driver.find_element(By.XPATH, "//*[@id='double-click']/h2")
action.double_click(doubleclick).perform()
