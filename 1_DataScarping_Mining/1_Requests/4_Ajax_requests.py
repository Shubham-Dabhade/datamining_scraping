import requests
import json

with open('ajax_data.txt','a',encoding='utf-8') as f:
    for i in range(1,6):

        r = requests.get(f"https://quotes.toscrape.com/api/quotes?page={i}")
        print(type(r.text)) # it is a string so convert it to iterate through it
        data = json.loads(r.text)

        for j in data['quotes']:
            f.write(j['author']['name'] + " | " + j['text'])
            f.write("\n")
