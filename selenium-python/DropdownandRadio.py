import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select



service = Service(executable_path="../drivers/chromedriver")
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://webdriveruniversity.com/")


wait = WebDriverWait(driver, 6)
button_clicks = driver.find_element(By.XPATH, "//*[@class='section-title']/h1[contains(text() ,'DROPDOWN, CHECKBOXE(S) & RADIO BUTTON(S)')]")
button_clicks.click()


parentwindow=driver.current_window_handle
child=driver.window_handles[1]
driver.switch_to.window(child)



dropdown1 = driver.find_element(By.ID, "dropdowm-menu-1")
sel=Select(dropdown1)
sel.select_by_value("python")


#radio


lettuce=driver.find_element(By.XPATH,"//*[@id='radio-buttons-selected-disabled']/input[1]")
if lettuce.is_enabled():
    lettuce.click()

time.sleep(4)