class ItemDiscount:
    def __init__(self, name, price):
        self._name_product = name
        self._price = price

    def set_price(self, new_price):
        self._price = new_price

    def get_info(self):
        print(f'Продукт: {self._name_product}\nЦена: {self._price}')


class ItemDiscountReport1(ItemDiscount):
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount

    def __str__(self):
        self._price = self._price*((100-self.discount)/100)
        return f'Продукт: {self._name_product}\nЦена: {self._price}'

    def get_parent_data(self):
        print(f'Продукт: {self._name_product}\nЦена: {self._price}')

    def get_info(self):
        print(f'Продукт: {self._name_product}')


class ItemDiscountReport2(ItemDiscount):
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount

    def __str__(self):
        self._price = self._price*((100-self.discount)/100)
        return f'Продукт: {self._name_product}\nЦена: {self._price}'

    def get_parent_data(self):
        print(f'Продукт: {self._name_product}\nЦена: {self._price}')

    def get_info(self):
        print(f'Цена: {self._price}')


if __name__ == '__main__':
    ob = ItemDiscount('Prod', 1000)
    ob1 = ItemDiscountReport1('Prod', 1000, 20)
    ob2 = ItemDiscountReport2('Prod', 1000, 20)

    print(ob.get_info())
    print(ob1.get_info())
    print(ob2.get_info())
    # ob.get_parent_data()
