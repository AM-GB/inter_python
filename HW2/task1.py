class ItemDiscount:
    def __init__(self, name, price):
        self.name_product = name
        self.price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(f'Продукт: {self.name_product}\nЦена: {self.price}')


if __name__ == '__main__':
    ob = ItemDiscountReport('Prod', 1500)

    ob.get_parent_data()
