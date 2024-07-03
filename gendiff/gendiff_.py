import argparse

from gendiff.building_difference_tree import difference_tree
from gendiff.formatters.stylish import formatter_stylish
from gendiff.parsing_date import read_and_parse_file


def main():
    args = get_args()
    print(
        generate_diff(args.first_file, args.second_file, args.format)
        # generate_diff(args.first_file, args.second_file, args.format)
    )


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


def get_formatter(formatter: str) -> callable:
    match formatter:
        case 'stylish':
            return formatter_stylish
        # case 'plain':
        #     return formatter_plain
        # case 'json':
        #     return formatter_json
        case _:
            raise ValueError(
                "The provided format is incorrect.."
                "Only the formats STYLISH, PLAIN, and JSON are supported."
            )


def generate_diff(file_path1: str, file_path2: str,
                  formatter: str = "stylish") -> str:
    file_1 = read_and_parse_file(file_path1)
    file_2 = read_and_parse_file(file_path2)
    ast = difference_tree(file_1, file_2)
    get_format = get_formatter(formatter)
    result = get_format(ast)
    return result
