from functions import gather_data, get_data_product, write_to_csv


def main():
    # сбор данных
    data = gather_data()
    # подготовка данных для записи
    products = get_data_product(data)
    # запись данных в csv file
    write_to_csv(products)


if __name__ == '__main__':
    main()
