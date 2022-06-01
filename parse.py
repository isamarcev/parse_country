import requests
from bs4 import BeautifulSoup


url = 'https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B3%D0%BE%D1%81%D1%83%D0%B4%D0%B0%D1%80%D1%81%D1%82%D0%B2'


def get_html(url):
    r = requests.get(url)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    pictures = soup.find('table').find_all('span', class_='flagicon')
    global items; items = []
    for item in pictures:
        items.append({
            'country': item.find('a', class_='image').get('title'),
            'full_country_name': item.find_parent().find_next_sibling().find_next_sibling().get_text().rstrip(),
            'flag_url': item.find('img', class_='thumbborder').get('src'),
            'same_letter_count': int,
        })
    letter_count = []
    for item in items:
        for keys, values in item.items():
            if keys == 'country':
                letter_count.append(values[0])
    for item in items:
        item['same_letter_count'] = letter_count.count(item['country'][0])
    print(items)
    return items

def parse():
    html = get_html(url)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print("error")


parse()


def find_country(items):
    x = input('Введите короткое название страны для показа инфо, "стоп" или 1 для выхода: ')
    if x.lower() == 'стоп' or x.lower() == '1':
        print("Спасибо, что воспользовались услугами наших авиалиний", "До встречи", end='\n')
        pass
    else:
        for item in items:
            if x.title() == item['country']:
                print(item)
                print("Попробуем еще раз?")
                find_country(items)

find_country(items)
