"""
Task 3. Develop a random number generator.
The initial and final generation numbers passed to the function
(zero must be excluded). Fill in the data list and dictionary.
Dictionary keys must be created using the template: "elem_ <element_number>".
Display the contents of the created list and dictionary.

Example:
(
[18, 22, 21, 23, 18, 21, 19, 16, 18, 8],
{'elem_18': 18, 'elem_22': 22, 'elem_21': 21, 'elem_23': 23, 'elem_19': 19, 'elem_16': 16, 'elem_8': 8}
)

"""
import random


def random_number(start, end):
    num = random.randrange(start, end + 1)
    if num != 0:
        return num
    else:
        return random_number(start, end)

def generator(start, end):
    for _ in range(10):
        yield random_number(start, end)

def random_numbers(start, end):
    result_lst = []
    result_dict = {}
    for num in generator(start, end):
        result_lst.append(num)
        result_dict[f'elem_{num}'] = num
    return result_lst, result_dict

def __main__():
    print(random_numbers(-2, 2))

__main__()
