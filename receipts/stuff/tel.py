# -*- coding: utf-8 -*-
"""
"""
import numpy as np

from receipts.stuff.base import CreateText
from receipts.utils import pull

class Tel(CreateText):

    def __init__(self, locale):
        super().__init__()
        self.locale = locale
        self.json_name = 'area_code.json'
        self._data = pull(self.json_name, 'tel')
        self.area_codes = self._area_code_list()
        if not self.area_codes:
            raise FileNotFoundError('File: {} has not been found.'.format(self.json_name))
        self.domestic_prefix = '0'  # TODO: change to have relationship with self.locale
    
    def __call__(self):
        phone_num = self.tel_num()
        phone_num = self._add_symbol(phone_num)
        return phone_num

    def tel_num(self):
        area_code = np.random.choice(self.area_codes)
        code_len = len(str(area_code))
        city_num_len = 5 - code_len
        city_num = np.random.randint(
                10**(city_num_len - 1), 
                10**city_num_len
                )
        member_num = np.random.randint(1000, 10000)
        phone_num = '{}{}-{}-{}'.format(
                self.domestic_prefix,
                area_code,
                city_num,
                member_num
                )
        return phone_num

    def _area_code_list(self):
        return self._data.get('area_code')

    def _add_symbol(self, phone_num):
        symbols = ['TEL:', '電話']
        symbol = str(np.random.choice(symbols))
        return symbol * self._isChoice(0.1) + phone_num

    def _isChoice(self, probability):
        return np.random.choice([0, 1], p=[1-probability, probability])

if __name__ == '__main__':
    tel = Tel('ja')
    for _ in range(10000):
        print(tel())

