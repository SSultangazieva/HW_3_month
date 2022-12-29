from pprint import pprint
import re
import requests
from bs4 import BeautifulSoup

URL = "https://www.lamoda.ru/c/563/bags-sumki-chehli/"
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}


def get_html(url):
    req = requests.get(url, headers=HEADERS)
    return req


def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all('div', class_='x-product-card__card')
    bags = []
    for item in items:
        price = item.find('div', class_='x-product-card-description__microdata-wrap').find_all('span')

        bags.append({
            'brand': item.find('div', class_='x-product-card-description__brand-name').getText(),
            'link': 'https://www.lamoda.ru' + item.find('a', class_='x-product-card__link').get('href'),
            'price': price[0].getText() if len(price) == 1 else price[1].getText()
        })
    return bags


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        answer = get_data(html.text)
        return answer
    else:
        raise Exception('Error in parser')