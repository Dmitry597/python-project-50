from gendiff import generate_diff
import pytest


def read(file_path):
    with open(file_path, 'r') as f:
        return f.read()


# пути к файлам json and yml для проверки
file1_json = 'tests/fixtures/file1.json'
file2_json = 'tests/fixtures/file2.json'
filepath1_yml = 'tests/fixtures/filepath1.yml'
filepath2_yml = 'tests/fixtures/filepath2.yml'

# чтение текстовых файлов для утверждения
check_json_and_yml = read('tests/fixtures/check_json_and_yml.txt')


test_gen_diff_cases = [
    (file1_json, file2_json, check_json_and_yml),
    (filepath1_yml, filepath2_yml, check_json_and_yml),
    (file1_json, filepath2_yml, check_json_and_yml)
]


@pytest.mark.parametrize('file_path1, file_path2, result', test_gen_diff_cases)
def test_gen_diff(file_path1, file_path2, result):
    assert generate_diff(file_path1, file_path2) == result

# команды для праверки
# gendiff tests/fixtures/file1.json tests/fixtures/file2.json
# gendiff tests/fixtures/filepath1.yml tests/fixtures/filepath2.yml
# gendiff tests/fixtures/file1.json tests/fixtures/filepath2.yml
# gendiff
