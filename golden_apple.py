import csv
import re
import time
from math import ceil
import tqdm
import requests
from data_for_request_products import (cookies, headers, json_data,
                                       url_products, url_card_product, params)


class GoldenAppleParse:

    @staticmethod
    def get_page_data(page=1):
        """
        POST запрос страницы из каталога
        :return: response в формате json (одна страница)
        """
        json = json_data
        json['pageNumber'] = page
        response = requests.post(
            url_products,
            cookies=cookies,
            headers=headers,
            json=json
        )
        while True:
            try:
                if response.status_code == 200:
                    return response.json()
                return response.status_code
            except requests.exceptions.ConnectionError:
                print('Проблема с соединением')
                time.sleep(1)

    def gather_data(self):
        """
        Получить список всех продуктов из каталога
        :return: список продуктов
        """
        # получить продукты из первой страницы (первый request)
        response = self.get_page_data()['data']
        products = response['products']
        # количество элементов на странице
        count_products_on_page = len(products)
        # Получить количество страниц
        pages = ceil(response['count'] / count_products_on_page)
        # получить остальные продукты
        for page in tqdm.tqdm(range(2, 3 + 1)):
            products += self.get_page_data(page)['data']['products']
        return products

    @staticmethod
    def get_product_card(product_id: int):
        """
        GET запрос карта продукта
        :param product_id:
        :return: картa продукта
        """
        param = params
        param['itemId'] = product_id
        response = requests.get(url=url_card_product,
                                params=param,
                                cookies=cookies,
                                headers=headers)
        while True:
            try:
                if response.status_code == 200:
                    return response.json()['data']
                return response.status_code
            except requests.exceptions.ConnectionError:
                print('Проблема с соединением')
                time.sleep(1)

    def get_data_product(self, lst_products: list):
        """
        Подготовить данные для записи в csv file
        :param lst_products:
        :return: данные для записи в csv file
        """
        products = []
        for product in tqdm.tqdm(lst_products):
            card = self.get_product_card(product['itemId'])
            item = {
                'url': f'https://goldapple.ru/{product["url"]}',
                'name': card["name"],
                'price': card['variants'][0]['price']['actual']['amount'],
                'rating': product.get('reviews', 'Нет рейтинга'),
            }

            if item['rating'] != 'Нет рейтинга':
                rating = item['rating'].get('rating')
                reviews_count = item['rating'].get('reviewsCount')
                item['rating'] = (f"Рейтинг: {rating}\n"
                                  f"Количество отзывов: {reviews_count}")
            for c in card['productDescription']:
                if c["text"] == 'описание':
                    item['description'] = self.clean_text(c['content'])
                if c["text"] == 'о бренде':
                    item['manufacturer_country'] = c['subtitle']
                if c['text'] == 'применение':
                    item['instructions'] = self.clean_text(c['content'])
                if (c["text"] == 'Дополнительная информация' and not item.
                        get("manufacturer_country")):
                    item['manufacturer_country'] =\
                        c['content'].split('<br>')[1]
            products.append(item)
        return products

    @staticmethod
    def write_to_csv(items: list):
        """
        запись в CSV файл c помощью DictWriter
        :param items:
        :return: None
        """
        with open('products.csv', 'w', newline='') as csvfile:
            fieldnames = ['name', 'description', 'manufacturer_country',
                          'instructions', 'price', 'rating', 'url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                    dialect='unix')
            writer.writeheader()
            writer.writerows(items)
        return True

    @staticmethod
    def clean_text(text: str):
        """
        очистка текста
        :param text:
        :return: Очищенный текст
        """
        # Удаление тегов HTML
        cleaned_text = re.sub('<.*?>', '', text)
        # Удаление лишних пробелов
        cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
        return cleaned_text.strip()
