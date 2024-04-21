import pandas as pd
import requests

authors=[]
quotes=[]

for i in range(1,11):
    r = requests.get(f'https://quotes.toscrape.com/page/{i}/')
    html = r.text
    print(f"this is the {i}th iteration")
    for data in html.split("\n"):
        if '<span class="text" itemprop="text">' in data:
            line = data.replace('<span class="text" itemprop="text">“','').replace('”</span>','')
            line = line.strip()
            quotes.append(line)

        if '<small class="author" itemprop="author">' in data:
            line = data.replace('<span>by <small class="author" itemprop="author">','').replace('</small>','')
            line = line.strip()
            authors.append(line)


data = pd.DataFrame({'author':authors, 'quotes':quotes})
data.to_csv("authors_quotes.csv",header=False,index=False)