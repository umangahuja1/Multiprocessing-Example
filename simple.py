import requests
from bs4 import BeautifulSoup
from time import sleep

base_url = 'http://quotes.toscrape.com/page/'

all_urls = list()

def generate_urls():
    for i in range(1,11):
        all_urls.append(base_url + str(i))
    
def scrape(url):
    res = requests.get(url)
    print(res.status_code, res.url)

generate_urls()
for url in all_urls:
    scrape(url)

    

