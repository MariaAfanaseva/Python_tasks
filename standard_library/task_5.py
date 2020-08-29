"""

5. Improve the first function from the previous example.

It is necessary to scan the text file created in the previous task
and implement creating and writing a new text file

Provide a new text file with lines of the form:

zmsebjvdgi zmsebjvdgi
ychpwljtzn ychpwljtzn
...

Those. fetches lines from the first text file
and in the new one they are written in the form where the string is put instead of a number

Regular expressions must be used here.

"""
import re


def create_new_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        with open('new_' + file_name, 'w', encoding='utf-8') as new_file:
            for line in file.readlines():
                search_result = re.search(r'([0-9]+) ([a-z]+)', line)
                num = search_result.group(1)
                word = search_result.group(2)
                new_line = line.replace(num, word)
                # new_line = re.sub('[0-9]+', word, line)
                # print(new_line)
                new_file.write(new_line)


create_new_file('task_4_file.txt')
