#!/usr/bin/env python3

import json


def formatter_json(root: dict) -> str:
    return json.dumps(root)
