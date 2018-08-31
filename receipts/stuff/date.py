# -*- coding: utf-8 -*-
"""
"""
import os
import sys

import mimesis
import numpy as np

from receipts.stuff.base import CreateText

class Date(CreateText):

    def __init__(self, locale):
        super().__init__()
        self.locale = locale
        self.week = [
                '日',
                '月',
                '火',
                '水',
                '木',
                '金',
                '土'
                ]

    def __call__(self):
        datetime = self.datetime()
        jp_datetime = self.parse_to_jp_datetime(datetime)
        jp_datetime += '({})'.format(
                self.week[datetime.weekday()]
                ) * self._isChoice(0.2)
        jp_datetime = self.prefix('注文日', 0.1) \
                + jp_datetime \
                + self.suffix('発行', 0.1)
        return jp_datetime

    def datetime(self):
        dt = mimesis.Datetime('ja')
        return dt.datetime()

    def parse_to_jp_datetime(self, datetime):
        parsed_datetime = '{}年{}月{}日'.format(
                datetime.year,
                datetime.month,
                datetime.day,
                )
        return parsed_datetime


    #def prefix(self, amount_of_money):
    #   symbol = ['注文日', '発行']
    #   choice = np.random.choice([0, 1], p=[0.5, 0.5])
    #   return '{}{}{}'.format(symbol[0]*choice, amount_of_money, symbol[1]*(1 - choice))

    def prefix(self, prefix_word, probability):
        return prefix_word * self._isChoice(probability)

    # TODO: no need to separate prefix and suffix
    def suffix(self, suffix_word, probability):
        return suffix_word * self._isChoice(probability)

    def _isChoice(self, probability):
        return np.random.choice([0, 1], p=[1-probability, probability])

if __name__ == '__main__':
    date = Date('ja')
    for _ in range(10000):
        print(date())

