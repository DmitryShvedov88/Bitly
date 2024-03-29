import requests
import os
import argparse


def shorten_link(headers, user_link):
    params = {"long_url": user_link}
    short_link = 'https://api-ssl.bitly.com/v4/bitlinks'
    response = requests.post(short_link, json=params, headers=headers)
    response.raise_for_status()

    return response.json()["id"]


def total_clicks(headers, user_link_short):
    summ_link = 'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    total_clicks_repl = summ_link.format(bitlink=user_link_short)
    response = requests.get(total_clicks_repl, headers=headers)
    response.raise_for_status()

    return response.json()["total_clicks"]


def is_bitlink(headers, user_link_short):
    cheak_link = 'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}'
    cheaker = cheak_link.format(bitlink=user_link_short)
    response = requests.get(cheaker, headers=headers)
    it_is_bitlink = response.ok

    return it_is_bitlink


def main():
    from dotenv import load_dotenv, find_dotenv
    from urllib.parse import urlparse
    load_dotenv(find_dotenv())

    parser = argparse.ArgumentParser()
    parser.add_argument('URL', help='Введите ссылку')

    name_url = parser.parse_args()
    user_link = format(name_url.URL)
    parsed_link=urlparse(user_link)
    user_link_short=parsed_link.netloc+parsed_link.path

    headers = {"Authorization": f'Bearer {os.getenv("BITLY_TOKEN")}'}

    if is_bitlink(headers, user_link_short):
        print('Колличество переходов по ссылки Битли:', total_clicks(headers, user_link_short))
    else:
        print(f'{parsed_link.scheme}://{shorten_link(headers, user_link)}')


if __name__ == "__main__":
    main()
