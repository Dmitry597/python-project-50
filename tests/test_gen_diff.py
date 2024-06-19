from gendiff import generate_diff


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


def test_gen_diff():
    check_gendiff = read(
        'tests/fixtures/check_gendiff.txt')
    assert generate_diff('gendiff/for_check_JSON_file/file1.json',
                         'gendiff/for_check_JSON_file/file2.json') == \
           check_gendiff
