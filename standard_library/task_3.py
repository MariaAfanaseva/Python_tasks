"""

3. Create two lists with different elements.
The first should contain the keys, the second - the values.
It is necessary to write a function that creates a dictionary
from the data of keys and values.
If the key lacks a value,
in the method, it must be stored as None.
Values ​​that did not have enough keys should be discarded.

For example, the function accepts two objects [3, 4, 5, 6], [44, 66, 56]
and returns {3: 44, 4: 66, 5: 56, 6: None}

"""
import random


def create_lst():
    return [random.randint(0, 100) for _ in range(random.randint(1, 10))]


def get_dict(lst_1, lst_2):
    # print(lst_1)
    # print(lst_2)
    result = {}
    for inx, data in enumerate(lst_1):
        try:
            result[data] = lst_2[inx]
        except IndexError:
            result[data] = None
    return result


print(get_dict(create_lst(), create_lst()))
