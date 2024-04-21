import requests

r = requests.get('https://quotes.toscrape.com')
print(r.status_code)

html = r.text
with open('quotes.txt','w') as f:
    for line in html.split("\n"):
        if '<span class="text" itemprop="text">' in line:
            line = line.replace('<span class="text" itemprop="text">“',"").replace('”</span>','')
            line = line.strip()
            f.write(line)
            f.write('\n')


# Quiz Extract Authors name
with open('authors.txt','w') as a:
    for author in html.split("\n"):
        if '<span>by <small class="author" itemprop="author">' in author:
            author = author.replace('<span>by <small class="author" itemprop="author">','').replace('</small>','')
            author = author.strip()
            a.write(author)
            a.write("\n")