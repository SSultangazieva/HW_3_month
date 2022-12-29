from pprint import pprint
import requests
from bs4 import BeautifulSoup

URL = "https://svetofor.info/sotovye-telefony-i-aksessuary/apple-iphone/?utm_source=site&utm_medium=all_categories"

# для создания имитации отправки запроса через браузер:
HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

# get запрос, чтобы получить себе html сайта:
def get_html(url):
    # отправить запрос через библиотеку requests
    req = requests.get(url=url, headers=HEADERS)
    return req

# парсить из полученного html
def get_data(html):
    # создаем объект класса BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser') #второй параметр-метод для парсинга (т.к. есть и др типа xml)
    items = soup.find_all('div', class_="grid-list asdads")
    #pprint(items)
    iphone = []
    for item in items:
        info = item.find('div', class_="grid-list asdads").find('div').string.split(', ')
        card = {
            'title': item.find('div', class_='front').find('a').string,
            'link': item.find('div', class_='front').find('a').get('href'),
            'price': item.find('span', class_='ty-price-num').find('a').get('href'),

        }
        iphone.append(card)
    return iphone
    pprint(iphone)




html = get_html(URL)
get_data(html.text)