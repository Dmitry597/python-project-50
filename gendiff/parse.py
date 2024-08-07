#!/usr/bin/env python3

import json
import yaml
import os

from gendiff.custom_exceptions import InvalidFormatError


def read_and_parse_file(file_path: str) -> [dict, None]:
    with open(file_path, 'r') as file_contents:
        return parse(file_contents, os.path.splitext(file_path)[1])


def parse(file_contents, file_format: str) -> [dict, None]:
    if file_format == '.json':
        return json.load(file_contents)
    elif file_format == '.yaml' or file_format == '.yml':
        return yaml.safe_load(file_contents)

    raise InvalidFormatError(
        "The file format is incorrect. "
        "Only files in JSON and YAML formats are supported."
    )
