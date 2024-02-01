Это приложение поможет определить, какие товары имеют для пользователя 
наибольшую ценность по совокупности параметров, чтобы:
  - закупить эти товары для продажи
  - активно продвигать их в рекламе и получать прибыль.

Приложение для сбора данных из  сайта https://goldapple.ru/parfjumerija.
Сохранение данных в CSV файл в текстовом формате.
Данные содержат:
    1. ссылка на продукт
    2. наименование
    3. цена
    4. рейтинг пользователей
    5. описание продукта
    6. инструкция по применению
    7. страна-производитель

Инструкция для запуск:
  - активировать виртуальное окружение ('sourse venv/bin/activate')
  - установить зависимости ('pip install -r requirements.txt')
  - запустить сбор данных данных ('python main.py')
  - получить готовый файл с данными под названием "products.csv"