from bs4 import BeautifulSoup  # importing beautiful soup module
import requests  # importing requests module

source = requests.get('https://www.dailymail.co.uk/ushome/index.html').text # getting info from source
soup = BeautifulSoup(source, 'lxml')  # parsing data from source

for article in soup.find_all('div', class_='article-tri-headline'): # running a loop to all articles

    # gathering headline information
    headline = article.h2.a.text 
    print()
    print('--- HEADLINE: ---')
    print(headline)
    print()

    # gathering summary information
    summary = article.p.text
    print('--- SUMMARY: ---')
    print(summary)
    print()

    # gathering url of full article
    video_source = soup.find('button')['data-url']
    video_url = video_source.split('?u=')[1]
    video_url_true = video_url.split('%3')[0]
    print('--- LINK TO FULL ARTICLE: ---')
    print(video_url_true)
    print()
    print('=======================')