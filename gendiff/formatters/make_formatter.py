from gendiff.custom_exceptions import InvalidFormatError
from gendiff.formatters.plain import formatter_plain
from gendiff.formatters.stylish import formatter_stylish
from gendiff.formatters.json import formatter_json


def get_formatter(formatter: str) -> callable:
    match formatter:
        case 'stylish':
            return formatter_stylish
        case 'plain':
            return formatter_plain
        case 'json':
            return formatter_json
        case _:
            raise InvalidFormatError(
                f'<{formatter}> The provided format is incorrect.. '
                'Only the formats STYLISH, PLAIN, and JSON are supported.'
            )
