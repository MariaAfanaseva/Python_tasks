"""

3. Improve the parent class in such a way
to access protected variables.

"""


class ItemDiscount:

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        print(f'Product name: {self.get_name()}, price: {self.get_price()}')


product_1 = ItemDiscountReport('Audi', 20000)
product_1.get_parent_data()
product_2 = ItemDiscountReport('BMW', 25000)
product_2.get_parent_data()

