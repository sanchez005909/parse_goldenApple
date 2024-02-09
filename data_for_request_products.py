url_products = "https://goldapple.ru/front/api/catalog/products"
url_card_product = "https://goldapple.ru/front/api/catalog/product-card"

cookies = {
    'ga-lang': 'ru',
    'client-store-code': 'default',
    'advcake_track_id': '06ed2f4f-a6dd-283e-10cc-ac92e2c9da7d',
    'advcake_session_id': 'a6f9a282-e7bb-8843-d13e-7659ff31d7ed',
    'mindboxDeviceUUID': '97ae5586-c18b-4018-ad0c-8fb5f53b229d',
    'directCrm-session': '%7B%22deviceGuid%22%3A%2297ae5586-c18b-4018-ad0c-'
                         '8fb5f53b229d%22%7D',
    'tmr_lvid': '50444076bee142b00b6d9eae0396f5ec',
    'tmr_lvidTS': '1706430708275',
    '_ym_uid': '1706430708909025359',
    '_ym_d': '1706430708',
    'adrcid': 'ALgR5jzp7vnkAkQ_P8Gbo8Q',
    'mage-cache-storage': '%7B%7D',
    'mage-cache-storage-section-invalidation': '%7B%7D',
    'form_key': 'EnnDiP90lmOWPGzf',
    'private_content_version': 'need_version',
    '_userGUID': '0:lrx920k2:TWaz~jgyihPUPk4QKghJSVVgJQH6xm2k',
    'gdeslon.ru.__arc_domain': 'gdeslon.ru',
    'gdeslon.ru.user_id': '89ec2e6a-375d-4c69-95d2-edb83c4fdc10',
    'recently_viewed_product': '%7B%7D',
    'recently_viewed_product_previous': '%7B%7D',
    'recently_compared_product': '%7B%7D',
    'recently_compared_product_previous': '%7B%7D',
    'product_data_storage': '%7B%7D',
    'adid': '170643116505236',
    'ga-plp-simple-layout': 'true',
    'opened_cart_route': 'https%253A%252F%252Fgoldapple.ru%252F',
    '__ddg1_': 'sUafjTTZ3D4oEuibqC99',
    'userId': '15690430',
    'access_token': 'eyJhbGciOiJSUzI1NiIsImtpZCI6IkE4QTdDRDBFNjE0REQxNzE1OTU0'
                    'ODZCNjA5MjNDMTBCRDYyMDZGMTRSUzI1NiIsInR5cCI6ImF0K2p3dCIs'
                    'Ing1dCI6InFLZk5EbUZOMFhGWlZJYTJDU1BCQzlZZ2J4USJ9.eyJuYmY'
                    'iOjE3MDY0NDQ0MzAsImV4cCI6MTczNzk4MDQzMCwiaXNzIjoiaHR0cHM6'
                    'Ly9wbGFpZC5nb2xkYXBwbGUucnUiLCJhdWQiOiJJbnRlcm5hbEFQSSIs'
                    'ImNsaWVudF9pZCI6ImNsaWVudF93ZWIiLCJzdWIiOiI3OTY4ODYwNjc'
                    '3MyIsImF1dGhfdGltZSI6MTcwNjQ0NDQzMCwiaWRwIjoicGhvbmVfY2F'
                    'sbF90b2tlbiIsIm1hZ2VudG9faWQiOiIxNTY5MDQzMCIsImN1c3RvbWV'
                    'yX2lkIjoiYzg2NzlhNGUtODUzNS00YWMxLWI4MzUtZWFiNmQ5YmY3ZjI'
                    'xIiwiY3VzdG9tZXJfcGhvbmUiOiI3OTY4ODYwNjc3MyIsImN1c3RvbWV'
                    'yX2lzX3JlZ2lzdGVyZWQiOiIwIiwiY3VzdG9tZXJfZ3JvdXBfaWQiOiI'
                    'wIiwianRpIjoiNTc2MjlDNDBDQjk4ODlDMkZENTIzM0UzNjMxNEFBNjMi'
                    'LCJpYXQiOjE3MDY0NDQ0MzAsInNjb3BlIjpbIm9wZW5pZCIsInByb2Zp'
                    'bGUiLCJXZWJBUEkiLCJvZmZsaW5lX2FjY2VzcyJdfQ.5B-oo9fQrqvR'
                    '6ah1lZ4TmYlyfQ9LSFep8h4UJJk_bQbLq__gamS_oeTkrryTyREUNie'
                    '-CvqPSjthMG5LLOmbOWbQjh9glnXkt5JA50NysMcgQ7-7Ty8ZaSljlB'
                    'r5y5GyP_hJzYJLNnltE0gBAZjJm5_7d_7Qd5R-NZ7Y5SDCafrHd-NvH'
                    '-ABP_eyKQjFDhPiwPlSv7ltjGAZclGlWM9a1xPERLZaj9QIrEAU2bIc'
                    'Qva_vT8S15FgPgR7SoTZOJVkI3SA8D59CeKlIectPA35XWV7m2g9oaT'
                    'lboRAIXLr7vopAI8bSWD8L6wxIxyCDPC8_EdDVniciRBKjATOOOMnaz'
                    'Ty_ehlAWHCxIN5bE2HsznE3I68vfGVcTdKYPqL2Uuvp2a57v7y9R1Hw'
                    '-oCho_TthNn3sj7Y3Scjfu0aVZHrwbJ_-lHTW1YBpRW7ZYhortlBryW'
                    'KJZ5JsaJAsXBY1Z2QGT4qct0dfetEZlRv8nvdEqlIcDjipgYaQgHPxD'
                    'EDafV2UTqpB0U0TLHNqhlFNwYStCxGYVIl4nAk01_GVLU5hgIINpNc3'
                    'Es-wrTOP8q9xQZF_rrcX8rdRJyS7WsptdsXr8NT6oGWvOknr_qf57Oo'
                    '7MCQyoHQwPtnAR35lgLW52zbmBBMb3ykXPDotIUPwCpkuiTF0J11osO'
                    'Pfr6X5GyOPg',
    'has_access_token': 'true',
    'refresh_token': '4ABE2E87A6035EAE3819A6303328A8399ACB9B7B9C47A62E8B'
                     'C6688260B356B9',
    'has_refresh_token': 'true',
    'welcome-back-modal-prevent': '1',
    'PHPSESSID': '2076fa4b1edae08db7c7f4a3351308f8',
    'X-Magento-Vary': 'beb8155825958a54f52ed854e3f710d9a77deedb',
    'mage-cache-sessid': 'true',
    'mage-messages': '',
    '_gid': 'GA1.2.256882807.1706682161',
    '_ym_isad': '2',
    'DIGI_CARTID': '246977912',
    'digi-analytics-sessionId': 'yABipinwVRKgymuHdh7Ob',
    '_spx': 'eyJpZCI6ImFiMjQyMWE0LTI5ZTMtNDZiMS1iMjEyLTFiOWFhOTU5NzA5MyIs'
            'ImZpeGVkIjp7InN0YWNrIjpbMCwwXX19',
    '_ga': 'GA1.1.1903006080.1706430708',
    '_ga_QE5MQ8XJJK': 'GS1.1.1706686610.6.1.1706688435.0.0.0',
    'section_data_ids': '%7B%22geolocation%22%3A1706688431%2C%22adult_goods%2'
                        '2%3A1706688435%2C%22cart%22%3A1706688435%2C%22'
                        'directory-data%22%3A1706444487%2C%22customer%22%'
                        '3A1706444487%2C%22compare-products%22%3A1706444487%'
                        '2C%22last-ordered-items%22%3A1706444487%2C%22captcha%'
                        '22%3A1706444487%2C%22wishlist%22%3A1706682160%2C%22'
                        'multiplewishlist%22%3A1706444487%2C%22goldcards%22%3'
                        'A1706444487%2C%22recently_viewed_product%22%3A17064'
                        '44487%2C%22recently_compared_product%22%3A1706444487%'
                        '2C%22product_data_storage%22%3A1706444487%7D',
    'tmr_detect': '0%7C1706688437355',
}

headers = {
    'authority': 'goldapple.ru',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
    'content-type': 'application/json',
    'sec-ch-ua-platform': '"Linux"',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}

json_data = {
    'categoryId': 1000000007,
    'cityId': '5ffc7a97-fd25-464b-8bdb-2b87c6261881',
    'cityDistrict': None,
    'pageNumber': 1,
    'filters': [],
    'customerGroupId': '7',
}

params = {
    'itemId': '19000165299',
    'cityId': '5ffc7a97-fd25-464b-8bdb-2b87c6261881',
}
