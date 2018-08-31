# -*- coding: utf-8 -*-
"""
"""
import os
import json


DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data'))

def pull(file_name, data_category):
    file_path = os.path.join(DATA_DIR, data_category, file_name)
    with open(file_path, 'r') as f:
        json_data = json.load(f)
    return json_data

