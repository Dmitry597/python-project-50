#!/usr/bin/env python3


from gendiff.building_difference_tree import difference_tree
from gendiff.formatters.plain import formatter_plain
from gendiff.formatters.stylish import formatter_stylish
from gendiff.formatters.json import formatter_json
from gendiff.parsing_date import read_and_parse_file


def get_formatter(formatter: str) -> callable:
    match formatter:
        case 'stylish':
            return formatter_stylish
        case 'plain':
            return formatter_plain
        case 'json':
            return formatter_json
        case _:
            raise ValueError(
                f'"<{formatter}> The provided format is incorrect..'
                f'Only the formats STYLISH, PLAIN, and JSON are supported."'
            )


def generate_diff(file_path1: str, file_path2: str,
                  formatter: str = "stylish") -> str:
    file_1 = read_and_parse_file(file_path1)
    file_2 = read_and_parse_file(file_path2)
    ast = difference_tree(file_1, file_2)
    get_format = get_formatter(formatter)
    result = get_format(ast)
    return result
