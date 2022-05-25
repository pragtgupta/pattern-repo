import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service = Service(executable_path="../drivers/chromedriver")
driver = webdriver.Chrome(service=service)
driver.get("https://www.goibibo.com/")
driver.maximize_window()


#logo
logo=driver.find_element(By.CLASS_NAME, 'gi-header-logo__home').text
print(logo)


#login and signup
login=driver.find_element(By.ID, 'get_sign_in').text
print(login)


#hotels and flights
hotels=driver.find_element(By.XPATH, "//a[@class='nav-link .' and .//text()='Hotels']").text
print(hotels)

flights=driver.find_element(By.XPATH, "//a[@class='nav-link active' and .//text()='Flights']").text
print(flights)



#from
Login1=driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/div[2]/div/div[1]/div[1]/div/div/p")
Login1.click()
Login2=driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/div[2]/div/div[1]/div[1]/div/div[2]/div/input")
Login2.send_keys("delhi")
time.sleep(6)




#search
search=driver.find_element(By.XPATH, "//span[@class='sc-fHeRUh jHgPBA' and .//text()='SEARCH FLIGHTS']").text
print(search)

#student fare
driver.find_element(By.XPATH, "//span[@class='sc-gKclnd kDbVbq' and .//text()='student']").click()

#round trips
driver.find_element(By.XPATH, "//span[@class='sc-gsNilK dImRia' and .//text()='Round-trip']").click()


#products
products=driver.find_element(By.XPATH, "//a[@class='fb button orange padLR30 txtTransUpper marginB10 fltHpySrchBtn' and .//text()='VIEW ALL PRODUCTS']").text
print(products)


driver.close()


