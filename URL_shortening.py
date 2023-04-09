import requests
import os
import argparse


def shorten_link(user_link):
    headers = {"Authorization": os.getenv("BITLY_TOKEN")}
    params = {"long_url": user_link}
    short_link = 'https://api-ssl.bitly.com/v4/bitlinks'
    response = requests.post(short_link, json=params, headers=headers)
    response.raise_for_status()

    return response.json()["id"]


def total_clicks(user_link):
    headers = {"Authorization": os.getenv("BITLY_TOKEN")}
    summ_link = 'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    total_clicks_repl = summ_link.format(bitlink=user_link)
    response = requests.get(total_clicks_repl, headers=headers)
    response.raise_for_status()

    return response.json()["total_clicks"]


def is_bitlink(user_link):
    headers = {"Authorization": os.getenv("BITLY_TOKEN")}
    cheak_link = 'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}'
    cheaker = cheak_link.format(bitlink=user_link)
    response = requests.get(cheaker, headers=headers)
    it_is_bitlink = response.ok

    return it_is_bitlink


def main():
    from dotenv import load_dotenv, find_dotenv
    load_dotenv(find_dotenv())

    parser = argparse.ArgumentParser()
    parser.add_argument('URL', help='Введите ссылку')

    name_url = parser.parse_args()
    user_link = format(name_url.URL)

    if is_bitlink(user_link):
        print('Колличество переходов по ссылки Битли:', total_clicks(user_link))
    else:
        print(f'http://{shorten_link(user_link)}')


if __name__ == "__main__":
    main()
