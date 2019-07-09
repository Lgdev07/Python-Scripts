import requests, smtplib
from bs4 import BeautifulSoup

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

search = str(input('Type what you would like to download: ')).replace(' ', '%20')
search_url = 'https://www.thepiratebay.org/search/' + search + '/0/99/0'
page = requests.get(search_url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')    
titles = []
urls = []

for a in soup.find_all("div", attrs={'class': 'detName'}):
    titles.append(a.text)

for a in soup.find_all('a', href=True):
    if a['href'][:6] == 'magnet':
        urls.append(a['href'])

for title, url in zip(titles, urls):
    print (f'Found the Name:{title}\nFound the URL: {url}\n\n')
