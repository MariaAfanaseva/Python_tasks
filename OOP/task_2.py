"""

2. Encapsulate both parameters (name and price)
product of the parent class.
Make sure that when saving the current logic of the program
a error will be generated.

"""


class ItemDiscount:

    def __init__(self):
        self.__name = 'Car'
        self.__price = 20000


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        print(f'Product name: {self.__name}, price: {self.__price}')


shop = ItemDiscountReport()
shop.get_parent_data()
