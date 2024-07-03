import itertools


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
        value: any, spaces_count: int = 1,
        start_depth: int = 0, replacer: str = ' '):

    def iter_recurs(current_value, depth):
        if not isinstance(current_value, dict):
            return chang_boolean(current_value)

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


def сonverter_string(key: any, value: any,
                     condition: str, start_indent: str) -> str:
    symbol = '  '
    match condition:
        case 'deleted':
            symbol = '- '
        case 'added':
            symbol = '+ '
        case 'unchanged' | 'nested':
            symbol = '  '
    return f'{start_indent}{symbol}{key}: {value}'


def formatter_stylish(root: dict, depth: int = 1, depth_indent: int = 4,
                      replacer: str = ' ', spaces_count: int = 4,
                      offset_left: int = 2) -> str:

    diff_lines = []
    correct_spaces = depth * spaces_count - offset_left
    current_indent = replacer * (correct_spaces - offset_left)
    start_indent = replacer * correct_spaces

    for key, val in root.items():
        condition = root[key].get('type')
        value = root[key].get("value")
        get_value = format_dict_indent(value, spaces_count, depth_indent)
        if condition == 'nested':
            get_value = formatter_stylish(value, depth + 1,
                                          depth_indent + spaces_count)
            diff_lines.append(сonverter_string(key, get_value,
                                               condition, start_indent))
        elif condition == 'changed':
            get_old_value = format_dict_indent(root[key].get("old"),
                                               spaces_count, depth_indent)
            get_new_value = format_dict_indent(root[key].get("new"),
                                               spaces_count, depth_indent)

            diff_lines.append(сonverter_string(key, get_old_value,
                                               'deleted', start_indent))
            diff_lines.append(сonverter_string(key, get_new_value,
                                               'added', start_indent))
        else:
            diff_lines.append(сonverter_string(key, get_value,
                                               condition, start_indent))

    result_diff = \
        itertools.chain("{",
                        sorted(diff_lines,
                               key=lambda x:
                               x[spaces_count * depth:x.index(":")]),
                        [current_indent + "}"])

    return '\n'.join(result_diff)
