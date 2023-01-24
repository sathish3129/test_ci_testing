#! /usr/bin/env python

import string

from os import path, mkdir
from random import randint, choice, choices

# 
def create_file(file_path):
    with open(file_path, 'w') as file:
        for i in range(1, 100):
            file.write("".join([choice(string.ascii_lowercase) for x in range(0, randint(5, 10))]).capitalize() + "\n")


def main():
    num = 2
    letters = choices(string.ascii_uppercase, k=num)
    if not path.exists('logs'):
        mkdir('logs')
        
    for f in letters:
        file_path = f'file_{f}.txt'
        create_file(path.join('logs', file_path))


if __name__ == '__main__':
    main()
