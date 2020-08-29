"""

1. Write a program that will contain a function
to get the filename from the full path to it.

When calling the function,
the path to the file must be passed as an argument.
In the function, it is necessary to implement "extraction"
from this path of the file name (without the extension).

Example:
the function will accept the next line - '../mainapp/views.py'

Result:
views

"""
import re


def get_name(path):
    return re.search(r'\/([A-Za-z0-9_]+)\.', path).group(1)
    # return path.split('/')[-1].split('.')[0]


print(get_name('../mainapp/views.py'))
