"""

5. Calculate the price of a discounted product.

The discount amount must be passed as an argument to the child class.

Overload child class constructor methods
(the init method to which the variable should be passed is the discount),
and an overload of the str method of the child class.

In this method, the price should be recalculated and the result should be returned -
discount price of goods.

"""


class ItemDiscount:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def change_price(self, new_price):
        self.price = new_price

    def __str__(self):
        return f'Product name: {self.name}, price: {self.price}'


class ItemDiscountReport(ItemDiscount):

    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount

    def discount_price(self):
        return self.price - (self.price * (self.discount / 100))

    def __str__(self):
        return f'Product name: {self.name}, price: {self.discount_price()} ' \
            f'with discount: {self.discount}%'


print(ItemDiscountReport('AUDI', 20000, 10))
