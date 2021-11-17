import inspect
import os
import sys


def get_script_dir(follow_symlinks=True):
    if getattr(sys, 'frozen', False):
        path = os.path.abspath(sys.executable)
    else:
        path = inspect.getabsfile(get_script_dir)
    if follow_symlinks:
        path = os.path.realpath(path)
    return os.path.dirname(path)


def find_file(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
        return None


def get_filename(file):
    path_file = find_file(file, get_script_dir())
    return path_file.split('/')[-1].split('.')[0]


if __name__ == '__main__':
    print(get_filename('task3.py'))
