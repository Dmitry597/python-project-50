from gendiff.formatters.stylish import chang_boolean


def chang_value(value: any) -> str:
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return chang_boolean(value)


def get_change_message(condition: str, string_path: str, value: str,
                       value_old: str = None,
                       value_new: str = None):

    if condition == 'changed':
        return f"Property '{string_path}' was updated. " \
               f"From {value_old} to {value_new}"
    elif condition == 'deleted':
        return f"Property '{string_path}' was removed"
    elif condition == 'added':
        return f"Property '{string_path}' was added with value: {value}"


def formatter_plain(root: dict, path=None) -> str:
    if path is None:
        path = []

    diff_lines = []

    for key, val in root.items():
        ls = [*path]
        condition = root[key].get('type')
        ls.append(key)
        string_path = '.'.join(ls)

        if condition == 'nested':
            get_value = formatter_plain(root[key].get("value"), ls)
            diff_lines.append(get_value)
        elif condition != 'unchanged':
            line_changes = get_change_message(condition, string_path,
                                              chang_value(root[key].get("value")
                                                          ),
                                              chang_value(root[key].get('old')),
                                              chang_value(root[key].get('new')))
            diff_lines.append(line_changes)

    result_diff = sorted(diff_lines, key=lambda x: x[10:])

    return '\n'.join(result_diff)
