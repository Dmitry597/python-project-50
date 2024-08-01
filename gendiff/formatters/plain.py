#!/usr/bin/env python3

from gendiff.formatters.stylish import chang_boolean


def chang_value(value: any) -> str:
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return chang_boolean(value)


def formatter_plain(root: dict, path=None) -> str:
    if path is None:
        path = []

    diff_lines = []

    for key in root:
        ls = path + [key]

        condition = root[key].get('type')
        value = root[key].get("value")
        new_value = chang_value(value)

        string_path = '.'.join(ls)

        if condition == 'nested':
            get_value = formatter_plain(value, ls)

            diff_lines.append(get_value)
        elif condition == 'changed':
            value_new = chang_value(root[key].get('new'))
            value_old = chang_value(root[key].get('old'))

            diff_lines.append(f"Property '{string_path}' was updated. "
                              f"From {value_old} to {value_new}")
        elif condition == 'deleted':
            diff_lines.append(f"Property '{string_path}' was removed")
        elif condition == 'added':
            diff_lines.append(f"Property '{string_path}' "
                              f"was added with value: {new_value}")

    result_diff = sorted(diff_lines, key=lambda x: x[10:])

    return '\n'.join(result_diff)
