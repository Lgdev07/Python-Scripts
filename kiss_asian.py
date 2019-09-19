import requests, smtplib
from bs4 import BeautifulSoup
import cfscrape

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }

# search = str(input('Type what you would like to download: ')).replace(' ', '%20')
scraper = cfscrape.create_scraper()  # returns a CloudflareScraper instance
scraper = scraper.get("https://kissasian.sh/")  # => "<!DOCTYPE html><html><head>..."
soup = BeautifulSoup(scraper.content, 'html.parser')    
titles = []
urls = []

for i in soup.find_all("div", {"id": "tab-newest"}):
    divTags = i.find_all("div", {"style": "position:relative"})
    for tag in divTags:
        title = tag.find_all("span", {"class": "title"})
        genre = tag.find_all("a", {"class": "dotUnder"})
        for line in title:
            print (f'Name: {line.text}')
        for line in genre:
            print (f'Genre: {line.text}')
        print()
