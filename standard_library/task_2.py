"""

2. Write a program that asks the user for numbers.
She responds with a message, an integer or fractional number.
If it is fractional, it is necessary to compare numbers and after the decimal point.

Examples:

Enter a number: test
You entered not a number

Enter the number: 45
Number 45 - integer

Enter the number: 45.45
Number 45.45 - fractional
The left and right sides are the same

Enter the number: 45.34
Number 45.34 - fractional
The left and right sides do not match

"""


def check_number():
    data = input('Enter the number: ')
    try:
        number_int = int(data)
        print(f'Number {number_int} is an integer')
    except ValueError:
        try:
            number_float = float(data)
            print(f'Number {number_float} is fractional')
            num = data.split('.')
            if num[0].lstrip('-') == num[1].rstrip('0'):
                print('The left and right sides are the same.')
            else:
                print('The left and right sides are not the same.')
        except ValueError:
            print('You entered not a number')


check_number()
