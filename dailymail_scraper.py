from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.dailymail.co.uk/ushome/index.html').text 
soup = BeautifulSoup(source, 'lxml')

for article in soup.find_all('div', class_='article-tri-headline'):
    #print(article.prettify())

    headline = article.h2.a.text 
    print()
    print('--- HEADLINE: ---')
    print(headline)
    print()

    summary = article.p.text
    print('--- SUMMARY: ---')
    print(summary)
    print()

    video_source = soup.find('button')['data-url']
    video_url = video_source.split('?u=')[1]
    video_url_true = video_url.split('%3')[0]
    print('--- LINK TO FULL ARTICLE: ---')
    print(video_url_true)
    print()
    print('=======================')