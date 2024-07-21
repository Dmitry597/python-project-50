from gendiff import generate_diff
import pytest
import json


def read_file(file_path: str) -> str:
    with open(file_path, 'r') as f:
        return f.read()


def check_json_valid(string: str) -> str:
    try:
        json.loads(string)
        return 'Valid json'
    except json.JSONDecodeError:
        return 'Invalid json'


# пути к файлам json and yml для проверки
FILE_PATH = 'tests/fixtures/'

file1_json = 'file1.json'
file2_json = 'file2.json'
file3_json = 'file3.json'
file4_json = 'file4.json'

file1_yml = 'file_1.yml'
file2_yml = 'file_2.yml'
file3_yml = 'file_3.yml'
file4_yml = 'file_4.yml'


# чтение текстовых файлов для утверждения
check_json_and_yml = read_file(FILE_PATH + 'check_json_and_yml.txt')
check_json_yml_nested = read_file(FILE_PATH + 'check_json_yml_nested.txt')
check_format_plain = read_file(FILE_PATH + 'check_format_plain.txt')

test_gen_diff_cases = [
    (file1_json, file2_json, 'stylish', check_json_and_yml),
    (file1_yml, file2_yml, 'stylish', check_json_and_yml),
    (file1_json, file2_yml, 'stylish', check_json_and_yml),
    (file1_yml, file2_json, 'stylish', check_json_and_yml),

    (file3_json, file4_json, 'stylish', check_json_yml_nested),
    (file3_yml, file4_yml, 'stylish', check_json_yml_nested),
    (file3_json, file4_yml, 'stylish', check_json_yml_nested),
    (file3_yml, file4_json, 'stylish', check_json_yml_nested),

    (file3_json, file4_json, 'plain', check_format_plain),
    (file3_yml, file4_yml, 'plain', check_format_plain),
    (file3_json, file4_yml, 'plain', check_format_plain),
    (file3_yml, file4_json, 'plain', check_format_plain),

]


@pytest.mark.parametrize('file1, file2, formatter, result', test_gen_diff_cases)
def test_gen_diff(file1, file2, formatter, result):
    assert generate_diff(FILE_PATH + file1,
                         FILE_PATH + file2,
                         formatter) == result


@pytest.mark.parametrize('file1, file2, formatter, result', [
    (file1_json, file2_json, 'json', 'Valid json'),
    (file3_json, file4_yml, 'json', 'Valid json'),
])
def test_gen_diff_json(file1, file2, formatter, result):
    assert check_json_valid(generate_diff(FILE_PATH + file1,
                                          FILE_PATH + file2,
                                          formatter)) == result
