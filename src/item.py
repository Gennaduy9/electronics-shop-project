import csv


class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        self.message = 'Файл item.csv поврежден'

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if 0 < len(name) <= 10:
            self.__name = name
        else:
            raise Exception ("Длина наименования товара превышает 10 символов")


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        return self.quantity * self.price


    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        items = []
        expected_fields = ['name', 'price', 'quantity']  # список ожидаемых полей таблицы
        try:
            with open('C:\\Users\\Геннадий Михайлович\\PycharmProjects\\electronics-shop-project\\src\\items.csv',
                'r', encoding='windows-1251') as csvfile:
                reader = csv.DictReader(csvfile)
                if reader.fieldnames != expected_fields:  # проверяем, что имена полей соответствуют ожидаемым
                      raise InstantiateCSVError ('Файл item.csv поврежден')
                for row in reader:
                    name = str(row['name'])
                    price = int(row['price'])
                    quantity = int(row['quantity'])
                    items.append(cls(name, price, quantity))
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл item.csv')
        return items

    @staticmethod
    def string_to_number(string):
        return float(string.replace(',', '.'))

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity

