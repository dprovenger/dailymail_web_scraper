from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.dailymail.co.uk/ushome/index.html').text 
soup = BeautifulSoup(source, 'lxml')

article = soup.find('div', class_='article-tri-headline')
#print(article.prettify())

headline = article.h2.a.text 
print(headline)