import unittest
from data_for_tests import product_id, lst_products, test_text
from functions import get_page_data, gather_data, get_product_card, \
    get_data_product, clean_text


class FuncTest(unittest.TestCase):

    def test_get_page_data(self):
        self.assertEqual(type(get_page_data()), dict)
        self.assertEqual(len(get_page_data()['data']['products']), 24)
        self.assertFalse(get_page_data(10000)['data']['products'])
        self.assertEqual(get_page_data('fg'), 400)

    def test_gather_data(self):
        self.assertEqual(type(gather_data()), list)

    def test_get_product_card(self):
        self.assertEqual(type(get_product_card(product_id=product_id)), dict)
        self.assertNotEqual(get_product_card(product_id=1), 200)

    def test_get_data_product(self):
        self.assertEqual(
            type(get_data_product(lst_products=lst_products)), list)
        self.assertEqual(get_data_product(lst_products=lst_products), [{
                'url': 'https://goldapple.ru//'
                       '19000010695-les-eaux-d-un-instant-immense-peony',
                'name': 'LES EAUX D’UN INSTANT Immense Peony',
                'price': 7780,
                'rating': 'Рейтинг: 4.7\nКоличество отзывов: 13',
                'description': 'Нежность лепестков пиона воплощена в аромате'
                               ' Immense Peony, посвященном свободе, '
                               'безмятежности и ощущению блаженства.'
                               ' Цветочно-фруктовая композиция ANGEL SCHLESSER'
                               ' с идеальной гармонией нот сладкой клубники и'
                               ' изысканного пиона расслабляет, словно'
                               ' умиротворяющий момент дня, когда солнце тает'
                               ' над горизонтом и морем, окрашивая закатное'
                               ' небо в розовый цвет. Чарующий аромат ласкает,'
                               ' будто бархатный песок и прибрежные волны, '
                               'благодаря мягкой базовой ноте мускуса. '
                               'Парфюмер – Ane Ayo. Ключевые ноты: клубника,'
                               ' пион, мускус.',
                'instructions': 'Только для наружного применения.',
                'manufacturer_country': 'Испания'}]
        )

    def test_write_to_csv(self):
        self.assertTrue(get_data_product(lst_products=lst_products))

    def test_clean_text(self):
        self.assertEqual(clean_text(test_text),
                         'Предложения по улучшениям '
                         'Проблемы с качеством товара или сервиса '
                         'Вопросы по улучшению условий сотрудничества '
                         'или карьерному росту')
