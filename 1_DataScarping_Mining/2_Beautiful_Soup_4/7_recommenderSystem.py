import requests
from bs4 import BeautifulSoup
import pandas as pd

headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
url = "https://www.imdb.com/chart/top/"

userMovieName = input("Enter Movie: ").lower()

page = requests.get(url, headers = headers)

html = page.text
soup = BeautifulSoup(html,'html.parser')
list = soup.find('ul',{'class':"ipc-metadata-list"})
list_items = list.findAll("li")

def removingNumList(lis):
    newList = []
    for i in lis:
        ind = i.index(" ")
        newSt = i[ind+1:]
        newList.append(newSt)
    return newList


def removingNumString(st):
    ind = st.index(" ")
    newSt = st[ind+1:]

    return newSt

movie = []

for items in list_items:

    a = items.find("a",{'class':"ipc-title-link-wrapper"})
    mov_title = a.find('h3').string
    mov_title = removingNumString(mov_title).strip()
    mov_title = mov_title.lower()

    if mov_title == userMovieName:
        #getting the link for each movie
        a_movie = items.find('a',{'class':"ipc-title-link-wrapper"})
        movieUrl = f"https://www.imdb.com/{a_movie['href']}"
        res_2 = requests.get(movieUrl,headers=headers)
        html_2 = res_2.text

        soup2 = BeautifulSoup(html_2,'html.parser')
        ul_2 = soup2.find("ul",{'class':"ipc-metadata-list ipc-metadata-list--dividers-all title-pc-list ipc-metadata-list--baseAlt"})
        director = ul_2.find("a",{'class':"ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link"})
        director_link = director['href']
        director_name = director.text.strip() #*
        print(f"The Director is {director_name}")

        #going to directors link and finding known movies

        res_3 = requests.get(f"https://www.imdb.com/{director_link}",headers=headers)
        html_3 = res_3.text

        soup_3 = BeautifulSoup(html_3,'html.parser')
        div_div_div_movies = soup_3.find('div',{'data-testid':"nm_flmg_kwn_for"})
        div_div_movies = div_div_div_movies.find('div',{'data-testid':"shoveler-items-container"})
        div_movies = div_div_movies.findAll('div',{'class':"ipc-primary-image-list-card__content"})
        print("Recommended Movies of the director are:")
        for mo in div_movies:
            anchor_movies = mo.findAll("a")
            print(anchor_movies[0].string)


        break


