import unittest
from data_for_tests import (product_id, lst_products, test_text,
                            lst_products_for_write)
from golden_apple import GoldenAppleParse


class TestGoldenAppleParse(unittest.TestCase):

    def setUp(self):
        self.gap = GoldenAppleParse()

    def test_get_page_data(self):
        self.assertEqual(type(self.gap.get_page_data()), dict)
        self.assertEqual(len(self.gap.get_page_data()['data']['products']), 24)
        self.assertFalse(self.gap.get_page_data(10000)['data']['products'])
        self.assertEqual(self.gap.get_page_data('fg'), 400)

    def test_gather_data(self):
        self.assertEqual(type(self.gap.gather_data()), list)

    def test_get_product_card(self):
        self.assertEqual(
            type(self.gap.get_product_card(product_id=product_id)), dict)
        self.assertNotEqual(self.gap.get_product_card(product_id=1), 200)

    def test_get_data_product(self):
        self.assertEqual(
            type(self.gap.get_data_product(lst_products=lst_products)), list)

    def test_write_to_csv(self):
        self.assertTrue(self.gap.write_to_csv(lst_products_for_write), None)

    def test_clean_text(self):
        self.assertEqual(self.gap.clean_text(test_text),
                         'Предложения по улучшениям '
                         'Проблемы с качеством товара или сервиса '
                         'Вопросы по улучшению условий сотрудничества '
                         'или карьерному росту')


if __name__ == "__main__":
    unittest.main()
