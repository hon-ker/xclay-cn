#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__clay__'

from fastapi import UploadFile
from typing import List, Union

import json
import yaml
from collections import namedtuple


def to_namedtuple_form_str(data: str):
    json_dict = json.loads(data)
    return json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))


def to_namedtuple_from_dict(data: dict):
    # 将字典转换为 JSON 允许的类型，这里我们使用了json.dumps将字典转换为JSON字符串
    json_data = json.dumps(data)
    # 使用json.loads将JSON字符串转换为对象，使用object_hook将其转换为命名元组
    return json.loads(json_data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))


def to_backend_namedtuple_config(file='config.yaml'):
    with open(file, 'r') as stream:
        data = yaml.safe_load(stream)
    _config = {}
    for config_type, config_item in data.items():
        config_name = config_type
        config_value = {}
        for sub_item, sub_item_value_dict in config_item.items():
            if not isinstance(sub_item_value_dict, dict):
                value = sub_item_value_dict
            else:
                value = sub_item_value_dict.get("value")

            config_value[sub_item] = value
        _config[config_name] = config_value

    return to_namedtuple_from_dict(_config)
