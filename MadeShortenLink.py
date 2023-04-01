import requests
import os
import argparse
from requests.exceptions import MissingSchema
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def shorten_link(headers, params):
    short_link = 'https://api-ssl.bitly.com/v4/bitlinks'
    response = requests.post(short_link, json=params, headers=headers)
    response.raise_for_status()

    return response.json()["id"]

def total_clicks(headers, user_link):
    summ_link = 'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    total_clicks = summ_link.format(bitlink=user_link)
    response = requests.get(total_clicks, headers=headers)
    response.raise_for_status()

    return response.json()["total_clicks"]

def is_bitlink(headers, params, user_link):
    try:
        print(f'http://{shorten_link(headers, params)}')
    except requests.exceptions.HTTPError as error:
        print('Колличество переходов по ссылки Битли:', total_clicks(headers, user_link))

def main(nameURL):
    user_link = nameURL
    headers, params = {"Authorization": os.getenv("BITLY_TOKEN")}, {"long_url": user_link}

    try:
        response = requests.get(user_link)
        response.raise_for_status()
    except requests.exceptions.HTTPError as error:
        print("Ошибка ввода")
        exit("Can't get data from server:\n{0}".format(error))
    except MissingSchema:
        print('URL is not complete/bitlink')

    is_bitlink(headers, params, user_link)

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('URL', help='Введите ссылку')

    return parser

if __name__ == "__main__":
    parser = createParser()
    nameURL = parser.parse_args()

    if nameURL.URL:
        main(format(nameURL.URL))
    else:
        print("Ошибка ввода")

