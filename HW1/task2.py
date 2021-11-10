import inspect
import os
import sys
# from os import getcwd, listdir


def get_script_dir(follow_symlinks=True):
    if getattr(sys, 'frozen', False):
        path = os.path.abspath(sys.executable)
    else:
        path = inspect.getabsfile(get_script_dir)
    if follow_symlinks:
        path = os.path.realpath(path)
    return os.path.dirname(path)


def get_directory_contents(sPath):
    result = []
    content = os.listdir(sPath)

    for c in content:
        if os.path.isdir(f'{sPath}/{c}'):
            result.append(print_directory_contents(f'{sPath}/{c}'))
        result.append(f'{sPath} : {c}')

    return result


def print_directory_contents(sPath):
    contents = get_directory_contents(sPath)

    for c in contents:
        print(c)


if __name__ == '__main__':
    # tree = os.walk(get_script_dir())

    # for d in tree:
    #     print(d)

    print('\n' + '*'*100 + '\n' + 'My result' + '\n' * 2)

    print_directory_contents(get_script_dir())
