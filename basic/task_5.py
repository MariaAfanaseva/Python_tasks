"""

Task 5 *. Improve the program "Bank deposit".
The third argument to the function must be a fixed
monthly amount of deposit replenishment. Needed in main function
implement a nested function for calculating interest for the replenished amount.
We assume that the client deposits funds on the last day of each month,
except for the first and last. For example, with a deposit term of 6 months
replenishment occurs within 4 months. The nested function returns
the amount of additional funds deposited (with interest),
and the main function is the total amount of the deposit at the end of the period.

Note: using a functional approach (not OOP)
Example: 10,000 for 24 months, replenishment - 100 each
chargable_deposit (10000, 24, 100)
by the end of the term: 13739.36

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

def deposit_capitalization(sum, term, amount_month=0):
    if check_data(sum, term):
        result = sum
        for product in PRODUCTS:
            if product['begin_sum'] <= sum < product['end_sum']:
                for month in range(term):
                    result += result * (product[term] / 100 / 12)
                    if month not in (0, term - 1):
                        result += amount_month
                print(f'Sum with capitalization: {round(result, 2)}')

deposit_capitalization(10000, 24, 100)
