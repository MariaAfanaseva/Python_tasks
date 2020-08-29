"""

Task 4. Write a program "Bank deposit".
It should consist of functions and their call with arguments.
The bank's client makes a deposit for a certain period.
Depending on the amount and term of the deposit, it is determined
interest rate:

1,000–10,000
(6 months - 5% per annum, a year - 6% per annum, 2 years - 5% per annum).

10,000-100,000
(6 months - 6% per annum, a year - 7% per annum, 2 years - 6.5% per annum).

100,000-1,000,000
(6 months - 7% per annum, a year - 8% per annum, 2 years - 7.5% per annum).

It is necessary to write a function to which parameters will be passed:
deposit amount and deposit term. Each of the three banking products must
be represented as a dictionary with keys (begin_sum, end_sum, 6, 12, 24).
The keys correspond to the values ​​of the beginning and end of the deposit amount and
interest rate values ​​for each term. The function needs
check if the deposit amount belongs to one of the ranges and
carry out the calculation at the desired interest rate. The function returns
deposit amount at the end of the term.

Note: a functional approach is used (not OOP).
You can make a calculation without capitalization and with capitalization

Example without capitalization: 10 thousand for 24 months
deposit (10000, 24)
by the end of the term: 11300

Example with capitalization (monthly): 10 thousand for 24 months
deposit (10000, 24)
by the end of the term: 11384.29

"""

PRODUCTS = [
    {'begin_sum': 1000, 'end_sum': 10000, 6: 5, 12: 6, 24: 5},
    {'begin_sum': 10000, 'end_sum': 100000, 6: 6, 12: 7, 24: 6.5},
    {'begin_sum': 100000, 'end_sum': 1000000, 6: 7, 12: 8, 24: 7.5}
]

def check_data(sum, term):
    if sum < PRODUCTS[0]['begin_sum'] or sum > PRODUCTS[-1]['end_sum']:
        print('Amount must be from 1000 to 1000000.')
        return False
    if term not in (6, 12, 24):
        print('Month must be 6, 12 or 24.')
        return False
    return True

def deposit(sum, term):
    if check_data(sum, term):
        for product in PRODUCTS:
            if product['begin_sum'] <= sum < product['end_sum']:
                result = sum * (1 + (product[term] / 100) * term / 12)
                print(f'Sum without capitalization: {round(result, 2)}')

def deposit_capitalization(sum, term):
    if check_data(sum, term):
        for product in PRODUCTS:
            if product['begin_sum'] <= sum < product['end_sum']:
                result = sum * ((1 + product[term] / (12 * 100)) ** term)
                print(f'Sum with capitalization: {round(result, 2)}')

deposit(10000, 24)
deposit_capitalization(1000, 24)
