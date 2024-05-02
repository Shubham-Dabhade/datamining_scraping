from selenium import webdriver

url = "https://www.google.com/"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get(url)

driver.quit()