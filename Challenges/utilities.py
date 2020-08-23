"""Utilities."""


def read_txt_file(path) -> list:
    """Reader.
    path: path file
    """
    open_file = open(path, 'r')
    file = open_file.read()
    file = file.split()
    return file
