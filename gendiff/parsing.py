import argparse
import json
import itertools
import yaml


def main():
    args = generate_diff_doc()
    print(
        generate_diff(args.first_file, args.second_file)
    )
    # generate_diff_doc()
    # print(
    #     generate_diff('gendiff/for_check_JSON_file/file1.json',
    #                   'gendiff/for_check_JSON_file/file2.json')
    # )    в ком.строке нужно будет указывать путь до файлов к примере -
    # gendiff tests/fixtures/file1.json tests/fixtures/file2.json # noqa


def generate_diff_doc() -> argparse.Namespace:
    """Функция получает аргументы из командной строки"""
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='''Compares two configuration
        files and shows a difference.''')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()

    return args


def сonverter_line(key: str, data: dict, diff=' ') -> str:
    """Функция преобразует строку в нужный формат и
    и адаптирует булевые значения к нужному наименованию """
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


def load_data_from_file(file_path: str) -> [str, None]:
    """Функция проверяет формат файла и исходя из этого
    преобразует в словарь Python"""
    if file_path.endswith('.json'):
        return json.load(open(file_path))

    if file_path.endswith('.yaml') or file_path.endswith('.yml'):
        return yaml.safe_load(open(file_path))

    raise ValueError(
        "The file format is incorrect. "
        "Only files in JSON and YAML formats are supported."
    )


def generate_diff(file_path1, file_path2):
    """Основная функция, которая сравнивает два файла и возвращает результат
    в виде строки"""
    file1 = load_data_from_file(file_path1)
    file2 = load_data_from_file(file_path2)
    intersection = file1.keys() & file2.keys()  # есть и там и там
    diff_file1 = file1.keys() - file2.keys()  # есть в первом, но нет во втором(-) # noqa: E501 <-- line too long
    diff_file2 = file2.keys() - file1.keys()  # есть во втором, но нет в первом(+) # noqa: E501 <-- line too long
    diff_ls_lines = []

    for i in intersection:
        if file1[i] == file2[i]:
            diff_ls_lines.append(сonverter_line(i, file1))
        else:
            diff_ls_lines.append(сonverter_line(i, file1, '-'))  # значение первого файла # noqa: E501 <-- line too long
            diff_ls_lines.append(сonverter_line(i, file2, '+'))  # значение второго файла(измененное) # noqa: E501 <-- line too long

    # 1 вариант
    # for i in diff_file1:
    #     diff_ls_lines.append(сonverter_line(i, file1, '-'))
    # for i in diff_file2:
    #     diff_ls_lines.append(сonverter_line(i, file2, '+'))

    # 2 вариант
    diff_ls_lines += (сonverter_line(i, file1, '-') for i in diff_file1)  # noqa: E501 <-- line too long
    diff_ls_lines += [сonverter_line(i, file2, '+') for i in diff_file2]  # noqa: E501 <-- line too long

    # 3 вариант
    # diff_ls_lines.extend(
    #     map(lambda x: сonverter_line(x, file1, '-'), diff_file1))
    # diff_ls_lines.extend(
    #     map(lambda x: сonverter_line(x, file2, '+'), diff_file2))

    result_diff = itertools.chain("{",
                                  sorted(diff_ls_lines, key=lambda x: x[4]),
                                  "}")

    return '\n'.join(result_diff)
