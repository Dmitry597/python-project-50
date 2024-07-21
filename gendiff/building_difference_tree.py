#!/usr/bin/env python3


def get_structure(key: str, value_one: any, value_two: any,
                  inner_tree_one: dict, inner_tree_two: dict) -> dict:
    if key not in inner_tree_one:
        return {'type': 'added',
                'value': value_two}
    elif key not in inner_tree_two:
        return {'type': 'deleted',
                'value': value_one}
    elif value_one == value_two:
        return {'type': 'unchanged',
                'value': value_one}
    else:
        return {'type': 'changed',
                'old': value_one,
                'new': value_two}


def difference_tree(tree_one: dict, tree_two: dict) -> dict:
    def join_tree(inner_tree_one: dict, inner_tree_two: dict) -> dict:
        root = dict()
        join_keys = inner_tree_one.keys() | inner_tree_two.keys()
        for key in join_keys:
            value_one = inner_tree_one.get(key)
            value_two = inner_tree_two.get(key)
            if (isinstance(value_one, dict) and isinstance(value_two, dict)) \
                    and value_one != value_two:
                root[key] = {'type': 'nested',
                             'value': join_tree(value_one, value_two)}
            else:
                root[key] = get_structure(key, value_one, value_two,
                                          inner_tree_one, inner_tree_two)
        return root

    result = join_tree(tree_one, tree_two)
    return result
