#!/usr/bin/python3


def read_file(filename=""):
    """reads filename with utf-8"""
    with open(filename, encoding='UTF-8') as f:
        print(f.read(), end="")
