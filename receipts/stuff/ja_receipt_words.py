# -*- coding: utf-8 -*-
"""
"""
import argparse
import datetime
import locale
import os
import sys
import random
from abc import abstractmethod, ABCMeta

import numpy as np

class ReceiptWords(object):
    """

    Args:
    """
    locale_list = [
            'ja'
            ]

    def __init__(self, locale='ja'):
        if not locale in self.locale_list:
            raise ValueError('This locale is not usable. Please select from {}'.format(
                self.locale_list
                ))

        self.locale = locale


    def datetime(self):
        return Date(self.locale)

    def currency(self):
        return Currency(self.locale)

    def tel(self):
        return Tel(self.locale)


class CreateText(metaclass=ABCMeta):

    @abstractmethod
    def __call__(self):
        pass

class Date(CreateText):

    def __init__(self, locale):
        super().__init__()
        self.locale = locale

    def __call__(self):
        pass

    def _create(self):
        pass

# TODO: make structure that easily can be customized to attach prefix and suffix
class Currency(CreateText):

    def __init__(self, locale):
        super().__init__()
        self.locale = locale

    def __call__(self, min_digit=10, max_digit=2000000, grouping=True):
        return self.prefix('ご請求額: ', 0.2) \
                + self._create(min_digit, max_digit, grouping) \
                + self.suffix('(含みます)', 0.2)

    def _create(self, min_digit, max_digit, grouping, suffix='-'):
        locale.setlocale(locale.LC_ALL, '')  # TODO: set locale using self.locale
        num = random.randint(min_digit, max_digit)
        currency = locale.currency(num, grouping=grouping)
        return currency + self._isChoice(suffix, 0.4)

    def prefix(self, prefix_word, probability):
        return prefix_word * self._isChoice(probability)

    def suffix(self, suffix_word, probability):
        return suffix_word * self._isChoice(probability)

    def _isChoice(self, probability):
        return np.random.choice([0, 1], p=[1-probability, probability])

def Tel(CreateText):

    def __init__(self, locale):
        super().__init__()
        self.locale = locale
    
    def __call__(self):
        pass
