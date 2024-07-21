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
file1_json = 'file1.json'
file2_json = 'file2.json'
file3_json = 'file3.json'
file4_json = 'file4.json'

file1_yml = 'file_1.yml'
file2_yml = 'file_2.yml'
file3_yml = 'file_3.yml'
file4_yml = 'file_4.yml'


# чтение текстовых файлов для утверждения
check_json_and_yml = read_file('tests/fixtures/check_json_and_yml.txt')
check_json_and_yml2 = read_file('tests/fixtures/check_json_and_yml2.txt')
check_format_plain = read_file('tests/fixtures/check_format_plain.txt')

test_gen_diff_cases = [
    (file1_json, file2_json, 'stylish', check_json_and_yml),
    (file1_yml, file2_yml, 'stylish', check_json_and_yml),
    (file1_json, file2_yml, 'stylish', check_json_and_yml),
    (file1_yml, file2_json, 'stylish', check_json_and_yml),

    (file3_json, file4_json, 'stylish', check_json_and_yml2),
    (file3_yml, file4_yml, 'stylish', check_json_and_yml2),
    (file3_json, file4_yml, 'stylish', check_json_and_yml2),
    (file3_yml, file4_json, 'stylish', check_json_and_yml2),

    (file3_json, file4_json, 'plain', check_format_plain),
    (file3_yml, file4_yml, 'plain', check_format_plain),
    (file3_json, file4_yml, 'plain', check_format_plain),
    (file3_yml, file4_json, 'plain', check_format_plain),

]


@pytest.mark.parametrize('file1, file2, formatter, result', test_gen_diff_cases)
def test_gen_diff(file1, file2, formatter, result):
    file_path = 'tests/fixtures/'
    assert generate_diff(file_path + file1,
                         file_path + file2,
                         formatter) == result


@pytest.mark.parametrize('file1, file2, formatter, result', [
    (file1_json, file2_json, 'json', 'Valid json'),
    (file3_json, file4_yml, 'json', 'Valid json'),
])
def test_gen_diff_json(file1, file2, formatter, result):
    assert check_json_valid(generate_diff(file1, file2, formatter)) == result

# команды для праверки
# gendiff tests/fixtures/file1.json tests/fixtures/file2.json
# gendiff tests/fixtures/file_1.yml tests/fixtures/file_2.yml
# gendiff tests/fixtures/file1.json tests/fixtures/file_2.yml

# gendiff tests/fixtures/file1.json tests/fixtures/file2.json
# gendiff tests/fixtures/file_1.yml tests/fixtures/file_2.yml
# gendiff tests/fixtures/file1.json tests/fixtures/file_2.yml
# gendiff tests/fixture/file_1.yml tests/fixtures/file2.json

# gendiff tests/fixtures/file3.json tests/fixtures/file4.json
# gendiff tests/fixtures/file_3.yml tests/fixtures/file_4.yml
# gendiff tests/fixtures/file3.json tests/fixtures/file_4.yml
# gendiff tests/fixtures/file_3.yml tests/fixtures/file4.json

# gendiff -f stylish tests/fixtures/file_3.yml tests/fixtures/file4.json


# gendiff -f plain tests/fixtures/file1.json tests/fixtures/file2.json
# gendiff -f plain tests/fixtures/file3.json tests/fixtures/file4.json
# gendiff -f plain tests/fixtures/file_3.yml tests/fixtures/file_4.yml
# gendiff -f plain tests/fixtures/file3.json tests/fixtures/file_4.yml

# gendiff -f json tests/fixtures/file1.json tests/fixtures/file2.json
# gendiff -f json tests/fixtures/file_3.yml tests/fixtures/file_4.yml
