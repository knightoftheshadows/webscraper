import requests
from bs4 import BeautifulSoup
import json

res = requests.get("https://www.kibeloco.com.br/")
res.encoding = "utf-8"
soup = BeautifulSoup(res.text, 'html.parser')

links = soup.find(class_="wp-pagenavi").find_all('a')

all_pages = []
for link in links:
    print(link.get('href'))
    page = requests.get(link.get('href'))
    soup = BeautifulSoup(page.text, 'html.parser')
    posts = soup.find_all(class_="apost")
    for post in posts:
        info = post
        title = info.h2.text
        preview = info.p.text
        all_pages.append({'title' : title, 'preview':preview})
print(len(all_pages))
with open('posts.json', 'w') as json_file:
    json.dump(all_pages, json_file, indent=3, ensure_ascii=False)
