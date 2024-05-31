import argparse
import json
import itertools


def main():
    generate_diff_doc()
    print(
        generate_diff('gendiff/for_check_JSON_file/file1.json',
                      'gendiff/for_check_JSON_file/file2.json')
    )


def generate_diff_doc():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='''Compares two configuration
        files and shows a difference.''')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    parser.parse_args()


def convert_line(key, data, diff=' '):
    match data[key]:
        case True:
            data[key] = 'true'
        case False:
            data[key] = 'false'
        case None:
            data[key] = 'null'

    match diff:
        case '-':
            return f'  - {key}: {data[key]}'
        case '+':
            return f'  + {key}: {data[key]}'
        case ' ':
            return f'    {key}: {data[key]}'


def generate_diff(file_path1, file_path2):
    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))
    intersection = file1.keys() & file2.keys()
    diff_file1 = file1.keys() - file2.keys()
    diff_file2 = file2.keys() - file1.keys()
    diff_ls_lines = []

    for i in intersection:
        if file1[i] == file2[i]:
            diff_ls_lines.append(convert_line(i, file1))
        else:
            diff_ls_lines.append(convert_line(i, file1, '-'))
            diff_ls_lines.append(convert_line(i, file2, '+'))

    for i in diff_file1:
        diff_ls_lines.append(convert_line(i, file1, '-'))

    for i in diff_file2:
        diff_ls_lines.append(convert_line(i, file2, '+'))

    result_diff = itertools.chain("{",
                                  sorted(diff_ls_lines, key=lambda x: x[4]),
                                  "}")
    return '\n'.join(result_diff)
