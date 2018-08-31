# -*- coding: utf-8 -*-
"""
"""
import os
import sys

import mimesis

from receipts.stuff.base import CreateText

class Date(CreateText):

    def __init__(self, locale):
        super().__init__()
        self.locale = locale

    def __call__(self):
        datetime = self.datetime()

    def datetime(self):
        dt = mimesis.Datetime('ja')
        return dt.datetime()

    def parse_to_jp_datetime(self, datetime):
        parsed_datetime = '{}年{}月{}日'.format(
                datetime.year,
                datetime.month,
                datetime.day
                )
        return parsed_datetime


if __name__ == '__main__':
    pass

