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
button_clicks = driver.find_element(By.XPATH, "//*[@class='section-title']/h1[contains(text() ,'AUTOCOMPLETE TEXTFIELD')]")
button_clicks.click()


parentwindow=driver.current_window_handle
child=driver.window_handles[1]
driver.switch_to.window(child)

driver.find_element(By.ID,"myInput").send_keys("P")
auto_complete_list=driver.find_elements(By.XPATH,"//*[@id='myInputautocomplete-list']/div/input")
option="Pepperoni"
time.sleep(2)
for i in auto_complete_list:
    print(i.get_attribute("value"))
    if i.get_attribute("value")==option:
        driver.execute_script("arguments[0].click();", i)
        break

