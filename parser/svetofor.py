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
    # найти карточки похожие
    items = soup.find_all('div', class_="ty-column4")
    iphone = []
    for item in items:
        # найти где описание
        info = item.find('div', class_="ty-grid-list__item-name").find('a')
        # добавить в список словарь с отбором
        iphone.append({
            "name": info.getText(),
            'link': info.get("href"),
            "price": item.find("span", class_="ty-price-num").getText(),
            "image": item.find("img", class_="ty-pict").get("data-ssrc")
        })
    return iphone
    pprint(iphone)

# запуск парсера:
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        iphone = []
        for i in range(1, 2):
            html = get_html(f"{URL}page-{i}/")
            current_page = get_data(html.text)
            iphone.extend(current_page)
        return iphone
    else:
        raise Exception("Bad request!")



# как вывести на экран для проверки:
# if __name__ == "__main__":
#     html = get_html(URL).text
#     pprint(get_data(html))