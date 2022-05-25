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
todobtn = driver.find_element(By.XPATH, "//div[@class='section-title']/h1[text()='TO DO LIST']")
todobtn.click()


parentwindow=driver.current_window_handle
child=driver.window_handles[1]
driver.switch_to.window(child)

input=driver.find_element(By.CSS_SELECTOR,"[type='text']")
input.send_keys("hello world",Keys.ENTER)
action=ActionChains(driver)
items=driver.find_elements(By.XPATH,"//ul/li")

for i in items:
    print(i.text)
    if i.text =="welcome":
        i.click()
        delete=i.find_element(By.XPATH,"span")
        action.move_to_element(delete).click(delete).perform()
        break



