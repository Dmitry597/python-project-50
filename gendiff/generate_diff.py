#!/usr/bin/env python3


from gendiff.building_difference_tree import difference_tree
from gendiff.formatters.make_formatter import get_formatter
from gendiff.parse import read_and_parse_file


def generate_diff(file_path1: str, file_path2: str,
                  formatter: str = "stylish") -> str:
    file_1 = read_and_parse_file(file_path1)
    file_2 = read_and_parse_file(file_path2)
    ast = difference_tree(file_1, file_2)
    get_format = get_formatter(formatter)
    result = get_format(ast)
    return result
