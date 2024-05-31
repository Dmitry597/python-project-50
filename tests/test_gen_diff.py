from gendiff import generate_diff


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


check_gendiff = read(
    'tests/fixtures/check_gendiff.txt')


def test_gen_diff():
    assert generate_diff('gendiff/for_check_JSON_file/file1.json',
                         'gendiff/for_check_JSON_file/file2.json') == \
           check_gendiff
