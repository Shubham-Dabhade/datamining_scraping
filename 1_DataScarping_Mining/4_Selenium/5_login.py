from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://quotes.toscrape.com/"

options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get(url)

#going on login page
driver.find_element(By.CSS_SELECTOR,'[href="/login"]').click()

#seleting and populating input fields
username = driver.find_element(By.CSS_SELECTOR,"#username")
password = driver.find_element(By.CSS_SELECTOR,"#password")

username.send_keys("Shubham")
time.sleep(3)
password.send_keys("12345")

time.sleep(3)
#submiting the login form
driver.find_element(By.CSS_SELECTOR,"[value='Login']").click()