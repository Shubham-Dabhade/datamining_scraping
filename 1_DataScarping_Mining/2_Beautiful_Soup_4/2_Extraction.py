from bs4 import BeautifulSoup
import requests

r = requests.get("https://quotes.toscrape.com/")
html = r.text

soup = BeautifulSoup(html, "html.parser")
#print(soup.title) # provides the first occurence of title tag
#print(soup.title.string) #provide the innerTEXT of the title tag
#print(soup.title.parent) #provides the whole parent tag
#print(soup.title.parent.name) #provied the name of the parent tag
#print(soup.findAll("span")) #finds all occurence of span tag

for i in soup.findAll("a"):
    print(i)