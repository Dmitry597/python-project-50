#!/usr/bin/env python3

import itertools


CHANGE_STATUS = {
    'deleted': '-',
    'added': '+',
    'unchanged': ' '
}


def chang_boolean(value: any) -> str:
    match value:
        case True:
            return 'true'
        case False:
            return 'false'
        case None:
            return 'null'
        case _:
            return str(value)


def format_dict_indent(
        value: any,
        spaces_count: int = 1,
        start_depth: int = 0
):

    def iter_recurs(current_value, depth):
        if not isinstance(current_value, dict):
            return chang_boolean(current_value)

        replacer = ' '
        deep_indent_size = depth + spaces_count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth

        lines = []

        for key, val in current_value.items():
            get_value = iter_recurs(val, deep_indent_size)
            lines.append(f'{deep_indent}{key}: {get_value}')
        result = itertools.chain("{", lines, [current_indent + "}"])

        return '\n'.join(result)

    return iter_recurs(value, start_depth)


def indent_formation(depth: int, spaces_count: int):
    replacer = ' '
    offset_left = 2
    correct_spaces = depth * spaces_count - offset_left
    current_indent = replacer * (correct_spaces - offset_left)
    start_indent = replacer * correct_spaces

    return start_indent, current_indent


def formatter_stylish(root: dict,
                      depth: int = 1,
                      depth_indent: int = 4,
                      ) -> str:

    spaces_count = 4
    start_indent, current_indent = indent_formation(depth, spaces_count)

    diff_lines = []

    for key in root:
        condition = root[key].get('type')
        value = root[key].get("value")
        get_value = format_dict_indent(value, spaces_count, depth_indent)

        if condition == 'nested':
            get_value = formatter_stylish(value,
                                          depth + 1,
                                          depth_indent + spaces_count)

            diff_lines.append(f'{start_indent}  {key}: {get_value}')
        elif condition == 'changed':
            old_value = root[key].get("old")
            new_value = root[key].get("new")

            get_old_value = format_dict_indent(old_value,
                                               spaces_count,
                                               depth_indent)
            get_new_value = format_dict_indent(new_value,
                                               spaces_count,
                                               depth_indent)

            diff_lines.append(f'{start_indent}- {key}: {get_old_value}')
            diff_lines.append(f'{start_indent}+ {key}: {get_new_value}')
        else:
            diff_lines.append(f'{start_indent}{CHANGE_STATUS[condition]} '
                              f'{key}: {get_value}')

    result_diff = \
        itertools.chain("{",
                        sorted(diff_lines,
                               key=lambda x:
                               x[spaces_count * depth:x.index(":")]),
                        [current_indent + "}"])

    return '\n'.join(result_diff)
