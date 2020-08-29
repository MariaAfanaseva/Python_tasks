"""

Check out the inheritance mechanism in Python.

To do this, create two classes. The first is the parent (ItemDiscount),
should contain static information about the product: name and price.

The second is a child (ItemDiscountReport),
should contain a function (get_parent_data) corresponding
for displaying product information in one line.

Check the operation of the program.

"""


class ItemDiscount:

    def __init__(self):
        self.name = 'Car'
        self.price = 20000


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        print(f'Product name: {self.name}, price: {self.price}')


shop = ItemDiscountReport()
shop.get_parent_data()
