"""

6.
Test the possibilities of polymorphism in practice.

You need to split the ItemDiscountReport child class into two classes.

It is optional to initialize the classes.

Inside each place a get_info function,
which in the first class will be responsible for displaying the name of the product,
and the second is its prices.

Next, implement the execution of each of the functions in three ways.

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

    @property
    def get_info(self):
        return f'Name: {self.get_name()}'


class ItemDiscountReportNew(ItemDiscount):

    @property
    def get_info(self):
        return f'Price: {self.get_price()}'


product_2 = ItemDiscountReportNew('AUDI', 25000)
print(product_2.get_info)
product_1 = ItemDiscountReport('BMW', 20000)
print(product_1.get_info)

for report in (product_1, product_2):
    print(report.get_info)


def print_info(product):
    print(product.get_info)


print_info(product_1)
print_info(product_2)
