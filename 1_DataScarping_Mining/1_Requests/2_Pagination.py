import requests

for i in range(1,11):
    r = requests.get(f'https://quotes.toscrape.com/page/{i}/')
    html = r.text

    with open('quotes.txt','a',encoding='utf-8') as f:
        for line in html.split("\n"):
            if '<span class="text" itemprop="text">' in line:
                line = line.replace('<span class="text" itemprop="text">“', "").replace('”</span>', '')
                line = line.strip()
                f.write(line)
                f.write('\n')
