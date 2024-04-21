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
genre = []
durations = []
va = 0
for items in list_items:
    print(f"Currently on this {va} iteration")
    if va == 10:
        break
    a = items.find("a",{'class':"ipc-title-link-wrapper"})
    mov_title = a.find('h3').string
    movie.append(mov_title)

    year = items.find("span",{'class':"sc-b189961a-8 kLaxqf cli-title-metadata-item"}).string
    years.append(year)

    rating = items.find("span",{'class':"ipc-rating-star"})
    ratings.append(rating['aria-label'][13:])


    #getting the link for each movie
    a_movie = items.find('a',{'class':"ipc-title-link-wrapper"})
    movieUrl = f"https://www.imdb.com/{a_movie['href']}"
    res_2 = requests.get(movieUrl,headers=headers)
    html_2 = res_2.text

    soup2 = BeautifulSoup(html_2,'html.parser')

    #getting duration
    ul_2 = soup2.find("ul",{'class':"ipc-inline-list ipc-inline-list--show-dividers sc-d8941411-2 cdJsTz baseAlt"})
    li = ul_2.findAll('li')
    duration = li[2].text.strip()
    durations.append(duration)

    #getting genre
    div = soup2.find('div',{'data-testid':'genres'})
    a_gen = soup2.findAll("a",{'class':'ipc-chip ipc-chip--on-baseAlt'})
    genres = []
    for a in a_gen:
        genres.append(a.text.strip())
    genres = ",".join(genres)
    genre.append(genres)

    va += 1


movies = removingNum(movie)

data = pd.DataFrame({'movie':movies,"year":years,"rating":ratings,'duration':durations,'genre':genre})
print(data)