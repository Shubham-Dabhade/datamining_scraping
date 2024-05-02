from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://quotes.toscrape.com/"

options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=options)
driver.get(url)

driver.find_element(By.CSS_SELECTOR,'.next a').click()