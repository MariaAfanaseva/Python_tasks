"""

4. Write a program in which to implement two functions.

The first should create a simple text file.
If a file with the same name already exists, display a corresponding message.

You need to open the file and prepare two lists: with textual and numerical information.
For example:
[91, 42, 47, 64, 60, 23, 82, 78, 22, 15]
and
['zmsebjvdgi', 'ychpwljtzn', 'zqywoopbwf', 'nkxdnnqyhe', 'eqpbrjwjdp',
'sllbegvgmh', 'kzrmrozeco', 'jbppumpypu', 'jjsmronkvm', 'qtnspcleqd']


Use generators to create lists. Apply the zip () function to the lists.
The result of this function must be processed and written to a file in such a way that
so that each line of the file contains a text and a numeric value.
For example:
91 zmsebjvdgi

42 ychpwljtzn

"""
import random

FILE_NAME = 'task_4_file.txt'


def create_numbers_lst():
    return [random.randint(0, 100) for _ in range(10)]


def create_words_lst():
    result = []
    word = ''
    for _ in range(10):
        for _ in range(8):
            word += chr(random.randint(97, 122))
        result.append(word)
        word = ''
    return result


def create_file(file_name):
    try:
        with open(file_name, 'x+', encoding='utf-8') as file:
            numbers_lst = create_numbers_lst()
            words_lst = create_words_lst()
            for i in range(10):
                file.write(f'{numbers_lst[i]} {words_lst[i]}\r')
    except FileExistsError:
        print('File already exists!')


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        print(file.read())


create_file(FILE_NAME)
read_file(FILE_NAME)
