import logging
import re
import json
import requests
import asyncio
import locale
import smtplib
import os
from datetime import datetime
from bs4 import BeautifulSoup


logger = logging.getLogger(__name__)

''' парсер для считывания данных с сайта kassy.ru '''


def created_mailing_list(urls):
    headers = {
        'Accept': '*/*',
        'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/102.0.0.0 Safari/537.36'
    }

    reg = r"^((http[s]:\/\/))?((\w*)|(\w*-\w*)).?(\w*).(\w*)\/(\w*)\/((\w*-\w*-\w*)|(\w*)|(\w*-\w*))\/(\d*.\d*)"
    req = requests.get(urls, headers=headers)
    with open('parser.html', 'w', encoding='utf-8') as file:
        file.write(req.text)

    with open('parser.html', encoding='utf-8') as file:
        src = file.read()
        soup = BeautifulSoup(src, 'html.parser')

    try:
        name_event = soup.find(class_='content').find('h1').find('a').string.lower()
    except Exception:
        name_event = 'Не нашли названия'

    try:
        rate = soup.find(class_='RARS').string
    except Exception:
        rate = 'нет ценза'

    try:
        date_event_all = soup.find(class_='venue').text.split('\n')[-2]
        date_event = ' '.join(date_event_all.split()[:2])
        time_event = soup.find(class_='venue').find('b').text
    except Exception:
        date_event = 'не нашли дату'
        time_event = 'не нашли время'

    try:
        venue = soup.find(class_='venue').find('a').string
    except Exception:
        venue = 'не нашли место'

    try:
        price = soup.find(class_='price_line').find('p').text.split(':')[1].replace('', '')
    except Exception:
        price = 'не нашли цену'

    try:
        number_phone_links = soup.find(id='city_phone').get('href')
        number_phone = soup.find(id='city_phone').text
    except Exception:
        number_phone = 'не нашли телефон'
        number_phone_links = 'не нашли ссылку на телефон'

    try:
        alert_date = soup.find(class_='message alert-danger').text
    except Exception:
        alert_date = 'Нет времени переноса'

    try:
        social = soup.find(id='social').find('a').get('href')
    except Exception:
        social = 'нет своих соцсетей'

    # поиск совместных мероприятий
    try:
        other_events = soup.find(class_='table repertuar').find_all(class_='order_ru order_modal')
        utm_metka = []
        for href_item in other_events:
            find_a = href_item['href']
            q_url = r"^(https?:\/\/\w*.\w*.\w*)"
            union_url = re.search(q_url, urls).group(1) + find_a
            metka = '__' + re.search(reg, union_url).group(13)
            utm_metka.append(metka)
        utm_labels = ''.join(utm_metka)
    except Exception:
        utm_labels = ''
    # try:
    #     description = soup.find(class_='announce').find_next(class_='price_line')
    # except Exception:
    #     description = 'Описание не найдено'

    # ^()?()()([\w\-\.]+[^#?\d]+)(.*)\/$
    # (?=(\w*)) - до точки
    # r"^()?()()([\w\-\.]+[^#?\d]+)(.*)\/$"
    # r"^((http[s]:\/\/))?(\w*).?(\w*).(\w*)\/(\w*)\/((\w*-.-\w*)|(\w*))\/(\d*.\d*)" - версия 2
    reg_ts = r"\d+(?=-(?!-))"
    reg_id = r"\d+$(?!-(?=-))"
    city = re.search(reg, urls).group(3)  # '{{subdivision}}'
    event_category = re.search(reg, urls).group(9)
    label = re.search(reg, urls).group(13)
    # ts_id = re.search(reg_ts, label)
    # id = re.search(reg_id, label)
    labels = '__' + label + utm_labels
    pixels = 'https://{{subdivision}}.kassy.ru/dispatch/view_{{dispatch_id}}.png?email={{email}}&token={{token}}'
    key = 'dispatch_id={{dispatch_id}}&email={{email}}&token={{token}}&user_id={{user_id}}'

    urls_data = {
        'link': urls,
        'city': city,
        'category': event_category,
        'title': name_event,
        # 'description': description,
        'rate': rate,
        'date': date_event,
        'time': time_event,
        'venue': venue,
        'price': price,
        'number_phone_links': number_phone_links,
        'number_phone': number_phone,
        'alert_date': alert_date,
        'labels': labels,
        'pixels': pixels,
        'key': key,
        'social': social,
    }

    return urls_data


''' распаковываем json в словарь для передачи в контекст '''

# def unpack(context):
#     with open('json_content.json', 'r', encoding='utf8') as file:
#         file = json.load(file)
#         for date in file['content']:
#             context.update(date['unchantedcontent'])
#             context.update(date['generalcontent'])
#             context.update(date['transfer'])
#     with open('json_url.json', 'r', encoding='utf-8') as file:
#         file = json.load(file)
#         for url in file:
#             context.update(url)
#     return context


# def unpuck_all(context):
#     with open('json_content.json', 'r', encoding='utf8') as file:
#         file = json.load(file)
#         for date in file['contents']:
#             context.update(date['UnchangedContent'])
#         for key, value in file.items():
#             if key in context:
#                 context[key].extend(value)
#             else:
#                 context[key] = value
#     return context


# функция сбора UTM меток
# def label_slice(content):
#     label = []
#     utm_met = []
#     for con in content:
#         label.append(con['labels'])
#         utm_met = list(set(label))
#     labels = ''.join(utm_met)
#     return labels


# def get_urls_content():
#     locale.setlocale(locale.LC_ALL, "ru")
#     ''' получение данных с API сайта Kassy '''
#     reg = r"^((http[s]:\/\/))?((\w*)|(\w*-\w*)).?(\w*).(\w*)\/(\w*)\/((\w*-\w*-\w*)|(\w*)|(\w*-\w*))\/(\d*.\d*)"
#     urls = 'https://ekb.kassy.ru/events/teatr/2-54914/'
#     city = re.search(reg, urls).group(3)
#     label = re.search(reg, urls).group(13)
#     event_category = re.search(reg, urls).group(9)
#
#     pixels = 'https://{{subdivision}}.kassy.ru/dispatch/view_{{dispatch_id}}.png?email={{email}}&token={{token}}'
#     key = 'dispatch_id={{dispatch_id}}&email={{email}}&token={{token}}&user_id={{user_id}}'
#
#     api_url = f'https://app-{city}.kassy.ru'
#
#     token = 'Ua2neix1ohTh1habieYideof3uy5pi'
#
#     auth_headers = {
#                     'accept': 'application/json',
#                     'Authorization': f'Token {token}',
#                     'Content-Type': 'application/x-www-form-urlencoded'
#                     }
#
#     auth_token = requests.post(f'{api_url}/api/kassy/v1/tokens', headers=auth_headers)
#
#     if auth_token.status_code != 200:
#         raise Exception('Error auth_token', 111)
#
#     auth_token = json.loads(auth_token.text)
#     connect_token = auth_token['content']['token']
#
#     headers = {'accept': 'application/json',
#                'Authorization': f'Token {connect_token}',
#                'Content-Type': 'application/x-www-form-urlencoded'
#                }
#
#     response = requests.get(f'{api_url}/api/kassy/v1/events/{label}', headers=headers)  # f'{api_url}/api/kassy/v1/events/70-31'
#     contact_response = requests.get(f'{api_url}/api/kassy/v1/contacts', headers=headers)
#
#     if response.status_code != 200:
#         raise Exception('Error response', 111)
#
#     if contact_response.status_code != 200:
#         raise Exception('Error contact_response', 111)
#
#     response = json.loads(response.text)
#     contact_response = json.loads(contact_response.text)
#
#     try:
#         date_time_get = response['content']['showtime']
#         date_object = datetime.strptime(date_time_get, '%Y-%m-%dT%H:%M:%S.%f%z')
#         date_event_ref = date_object.date()
#         time_event_ref = date_object.time()
#         date_event = date_event_ref.strftime('%d %b')
#         time_event = time_event_ref.strftime('%H:%M')
#     except Exception:
#         date_event = 'Не нашли дату'
#         time_event = 'Не нашли время'
#
#     try:
#         price = response['content']['min_price']
#     except Exception:
#         price = 'НЕ нашли цену'
#
#     try:
#         venue = response['content']['building']['title']
#     except Exception:
#         venue = 'Не нашли место'
#
#     try:
#         rate = response['content']['performance']['age_restriction']
#     except Exception:
#         rate = 'Не нашли ценз'
#
#     try:
#         name_event = response['content']['performance']['title']
#     except Exception:
#         name_event = 'Не нашли название'
#
#     try:
#         other_events = response['content']['other_events']
#         utm_metka = []
#
#         for labels in other_events:
#             id = '__' + labels['id']
#             utm_metka.append(id)
#         utm_labels = ''.join(utm_metka)
#     except Exception:
#         utm_labels = ''
#
#     labels = '__' + label + utm_labels
#
#     try:
#         social = contact_response['content']['social_links']['vk']
#     except Exception:
#         social = 'нет своих соцсетей'
#
#     try:
#         number_phone_get = contact_response['content']['contact_items']
#         number_phone = []
#         number_phone_liks = []
#         for number in number_phone_get[:1]:
#             number_phone = ''.join(number['phones'])
#             table_del = {ord('\n'): '', ord('('): '', ord(')'): '', ord(' '): '', ord('-'): ''}
#             number_phone_liks = 'tel:' + number_phone.translate(table_del)
#     except Exception:
#         number_phone = 'Не нашли телефон'
#         number_phone_liks = 'Нет ссылки на телефон'
#
#     urls_data = {
#         'poster_url': urls,
#         'banner_url': urls,
#         'name_event': name_event,
#         'date_event': date_event,
#         'time_event': time_event,
#         'city': city,
#         'event_category': event_category,
#         'venue': venue,
#         'price': price,
#         'rate': rate,
#         'number_phone': number_phone,
#         'number_phone_liks': number_phone_liks,
#         'labels': labels,
#         'social': social,
#         'pixels': pixels,
#         'key': key
#     }
#
#     return urls_data


