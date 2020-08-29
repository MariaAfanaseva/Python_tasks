"""

4. Implement the ability to change the product price value.

It is necessary for both parent and child classes to get a new price value.
You should check this by calling the corresponding method of the parent class
and the function of the child (function,
responsible for displaying information about the product in one line).

"""


class ItemDiscount:

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def change_price(self, new_price):
        self.__price = new_price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        print(f'Product name: {self.get_name()}, price: {self.get_price()}')


shop = ItemDiscountReport('AUDI', 20000)
shop.change_price(25000)
shop.get_parent_data()
