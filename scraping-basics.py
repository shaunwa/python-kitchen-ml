import requests
from bs4 import BeautifulSoup
import json

url = 'https://news.ycombinator.com'
response = requests.get(url)

html = response.text
soup = BeautifulSoup(html, 'html5lib')

articles = []

rows = soup.find_all('tr', class_='athing')
for row in rows:
    title_tag = row.find('span', class_='titleline')
    a_tag = title_tag.find('a')
    title = title_tag.text
    link_url = a_tag.get('href', 'N/A')

    next_row = row.find_next_sibling('tr')
    score_tag = next_row.find('span', class_='score')

    if score_tag:
        score = score_tag.text
    else:
        score = 'N/A'

    new_article = {
        'title': title,
        'link_url': link_url,
        'upvotes': score,
    }

    articles.append(new_article)

with open('hacker-news-articles.json', 'w') as file:
    json.dump(articles, file)