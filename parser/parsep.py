import requests
from bs4 import BeautifulSoup as BS
from pprint import pprint

URL = "https://hdrezka.ag/"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36"
}


def get_html(url):
    req = requests.get(url=url, headers=HEADERS)
    return req


def get_data(html):
    soup = BS(html, 'html.parser')
    items = soup.findAll('div', class_="b-content__inline_items")
    all_kino_list = []
    for item in items:
        kino = item.findAll("div", class_="b-content__inline_item")
        for i in kino:
            info = i.find("div", class_="b-content__inline_item-link").find("div").string.split(', ')
            all_kino = {
                "title": i.find("div", class_="b-content__inline_item-link").find("a").text,
                "link": i.find("div", class_="b-content__inline_item-link").find("a").get("href"),
                "year": info[0],
                "country": info[1],
                "genre": info[2],
                "status": i.find('span', class_='info').string
                if i.find('span', class_='info') is not None else "Полнометражка",
            }
            all_kino_list.append(all_kino)
    return pprint(all_kino_list)


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        cinematics = []
        html = get_html(f"{URL}page/1/")
        current_page = get_data(html.text)
        cinematics.extend(current_page)
        return cinematics
    else:
        raise Exception("Ошибка")


html = get_html(URL)
get_data(html.text)