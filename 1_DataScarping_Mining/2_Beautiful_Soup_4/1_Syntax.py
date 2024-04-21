from bs4 import BeautifulSoup
import requests

r = requests.get("https://quotes.toscrape.com/")
html = r.text

soup = BeautifulSoup(html, "html.parser")
print(soup)