from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://www.deepl.com/translator"

options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get(url)
time.sleep(3)
#closing the cookie pop up
driver.find_element(By.CSS_SELECTOR,".cookieBanner-module--cta_buttonClose--ojVnN button").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,".h-6 button").click()
#setting the language to be translated in
 ## getting the drop down

driver.find_element(By.CSS_SELECTOR,"[data-testid='translator-target-lang-btn']").click()

##selecting language
driver.find_element(By.CSS_SELECTOR,"[data-testid='translator-lang-option-ja']").click()

### Adding the input text
textarea = driver.find_element(By.CSS_SELECTOR,"[data-testid='translator-source-input']")
textarea.send_keys("Hello World")