from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

url = "https://quotes.toscrape.com/page/9/"

driver = webdriver.Chrome()
driver.get(url)


quotes = []
authors = []
tags = []
while True:
    for div in driver.find_elements(By.CSS_SELECTOR, ".quote"):

        quotes_span = div.find_element(By.TAG_NAME, 'span')
        author_small = div.find_element(By.CSS_SELECTOR, ".author")
        tags_a = div.find_elements(By.CSS_SELECTOR, ".tag")
        tags_auth = []
        for i in tags_a:
            tags_auth.append(i.text)

        tags_new = ",".join(tags_auth)

        quote = quotes_span.text
        author = author_small.text

        quotes.append(quote.strip())
        authors.append(author.strip())
        tags.append(tags_new)

    try:
        driver.find_element(By.CSS_SELECTOR,".next a").click()
    except:
        break


data = pd.DataFrame({"quotes": quotes, "authors": authors, 'tags': tags})
print(data)