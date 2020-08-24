"""

Task 2. Add the following function with the missing code:
def print_directory_contents (sPath):

    The function takes the name of the directory and prints out its contents
    in the form of "path and file name", as well as any other
    files in subdirectories.

    This function is similar to os.walk. Use os.walk function
    it is impossible. This task shows your ability to work with
    nested structures.

Example:
[
('mainapp', 'admin.py'),
('mainapp\\management\\commands', 'seed_db.py'),
...
]

"""
import os


def print_directory_contents(path, list):
    for name in os.listdir(path):
        if os.path.isfile(f'{path}/{name}'):
            list.append((path, name))
        else:
            print_directory_contents(f'{path}/{name}', list)
    return list

print(print_directory_contents('/GeekBrains/Python_interiew/test', []))
