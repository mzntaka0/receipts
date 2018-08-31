# -*- coding: utf-8 -*-
"""
"""
import os
import sys
import locale
import random

import numpy as np

from receipts.stuff.base import CreateText

# TODO: have to make it customizable e.g) using yaml, json [word, probability]...
class Currency(CreateText):

    def __init__(self, locale, min_digit=10, max_digit=1000000, grouping=True):
        super().__init__()
        self.locale = locale
        self.min_digit = min_digit
        self.max_digit = max_digit
        self.grouping = True

    def __call__(self):
        return self.prefix('ご請求額: ', 0.1) \
                + self._create() \
                #+ self.suffix('(含みます)', 0.1)

    def _create(self, beta_b=40, suffix='-'):
        locale.setlocale(locale.LC_ALL, '')  # TODO: set locale using self.locale
        num = self.amount_of_money(beta_b=beta_b)
        currency = self.add_symbol(num)
        return currency + (suffix * self._isChoice(0.4))

    def amount_of_money(self, beta_b=40):
        amount = max(self.min_digit, int(np.random.beta(1, beta_b) * self.max_digit))
        locale.setlocale(locale.LC_ALL, '')
        return locale.currency(amount, symbol=False, grouping=True)

    def add_symbol(self, amount_of_money):
       symbol = ['￥', '円']
       choice = np.random.choice([0, 1], p=[0.5, 0.5])
       return '{}{}{}'.format(symbol[0]*choice, amount_of_money, symbol[1]*(1 - choice))

    def prefix(self, prefix_word, probability):
        return prefix_word * self._isChoice(probability)

    def suffix(self, suffix_word, probability):
        return suffix_word * self._isChoice(probability)

    def _isChoice(self, probability):
        return np.random.choice([0, 1], p=[1-probability, probability])

    def jp_yen(self):
        return locale.currency(self.amount_of_money(), grouping=True)

    #def get_digit_number(self):
    #    digit_list = np.array([10**x for x in range(2, 7)])  # 100 - 1,000,000
    #    correct_list = np.array([1, 15, 20, 9, 1])
    #    ratio_list = [(1 / x) for x, y in zip(digit_list, correct_list)]
    #    money_distribution = ratio_list.copy() / sum(ratio_list)
    #    digit = np.random.choice(digit_list, p=money_distribution)
    #    print(digit)
    #    return digit

if __name__ == '__main__':
    a = Currency('ja')
    for _ in range(10000):
        print(a())
