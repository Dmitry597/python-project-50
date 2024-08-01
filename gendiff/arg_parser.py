#!/usr/bin/env python3

import argparse


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='''Compares two configuration
        files and shows a difference.''')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', default='stylish',
                        help='set format of output')
    args = parser.parse_args()

    return args
