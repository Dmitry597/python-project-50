from gendiff import generate_diff
import pytest
import json
import os


def read_file(file_path: str) -> str:
    with open(file_path, 'r') as f:
        return f.read()


def check_json_valid(string: str) -> str:
    try:
        json.loads(string)
        return 'Valid json'
    except json.JSONDecodeError:
        return 'Invalid json'


def get_absolute_path(file: str) -> str:
    absolute_path = os.path.join(os.path.dirname(__file__), 'fixtures', file)
    return os.path.realpath(absolute_path)


test_gen_diff_cases = [
    ('file1.json', 'file2.json', 'stylish', 'check_format_stylish.txt'),
    ('file_1.yml', 'file_2.yml', 'stylish', 'check_format_stylish.txt'),
    ('file1.json', 'file_2.yml', 'stylish', 'check_format_stylish.txt'),
    ('file_1.yml', 'file2.json', 'plain', 'check_format_plain.txt')
]


@pytest.mark.parametrize('file1, file2, formatter, result', test_gen_diff_cases)
def test_gen_diff(file1, file2, formatter, result):
    abs_path_result = get_absolute_path(result)
    correct_result = read_file(abs_path_result)

    abs_path_file1 = get_absolute_path(file1)
    abs_path_file2 = get_absolute_path(file2)

    assert generate_diff(abs_path_file1, abs_path_file2,
                         formatter) == correct_result


def test_gen_diff_json():
    abs_path_file1 = get_absolute_path('file1.json')
    abs_path_file2 = get_absolute_path('file_2.yml')

    assert check_json_valid(generate_diff(abs_path_file1, abs_path_file2,
                                          'json')) == 'Valid json'
