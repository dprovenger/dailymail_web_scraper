from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.dailymail.co.uk/ushome/index.html').text 
soup = BeautifulSoup(source, 'lxml')

article = soup.find('div', class_='article-tri-headline')
#print(article.prettify())

headline = article.h2.a.text 
print(headline)

summary = article.p.text
print(summary)

video_source = soup.find('button')['data-url']
video_url = video_source.split('?u=')[1]
video_url_true = video_url.split('%3')[0]
print(video_url_true)