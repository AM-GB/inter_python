class ItemDiscount:
    def __init__(self, name, price):
        self._name_product = name
        self._price = price

    def set_price(self, new_price):
        self._price = new_price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(f'Продукт: {self._name_product}\nЦена: {self._price}')


if __name__ == '__main__':
    ob = ItemDiscountReport('Prod', 1500)

    ob.set_price(2000)
    ob.get_parent_data()
