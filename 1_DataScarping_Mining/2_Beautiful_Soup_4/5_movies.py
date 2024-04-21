import requests
from bs4 import BeautifulSoup
import pandas as pd

headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
url = "https://www.imdb.com/chart/top/"

page = requests.get(url, headers = headers)

html = page.text
soup = BeautifulSoup(html,'html.parser')

list = soup.find('ul',{'class':"ipc-metadata-list"})
list_items = list.findAll("li")


def removingNum(lis):
    newList = []
    for i in lis:
        ind = i.index(" ")
        newSt = i[ind+1:]
        newList.append(newSt)
    return newList

movie = []
years = []
ratings = []
for items in list_items:
    a = items.find("a",{'class':"ipc-title-link-wrapper"})
    mov_title = a.find('h3').string
    movie.append(mov_title)

    year = items.find("span",{'class':"sc-b189961a-8 kLaxqf cli-title-metadata-item"}).string
    years.append(year)

    rating = items.find("span",{'class':"ipc-rating-star"})
    ratings.append(rating['aria-label'][13:])

movies = removingNum(movie)

data = pd.DataFrame({'movie':movies,"year":years,"rating":ratings})
print(data) 