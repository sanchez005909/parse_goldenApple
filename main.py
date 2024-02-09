from golden_apple import GoldenAppleParse


def main():
    gap = GoldenAppleParse()
    # сбор данных
    data = gap.gather_data()
    # подготовка данных для записи
    products = gap.get_data_product(data)
    # запись данных в csv file
    gap.write_to_csv(products)


if __name__ == '__main__':
    main()
