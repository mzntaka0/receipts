# -*- coding: utf-8 -*-
"""
"""
import argparse
import os
import sys
from abc import abstractmethod, ABCMeta
from pathlib import Path
try:
    from bpdb import set_trace
except ImportError:
    from pdb import set_trace

from receipts.stuff.base import CreateText

class Date(CreateText):

    def __init__(self, locale):
        super().__init__()
        self.locale = locale

    def __call__(self):
        pass

    def _create(self):
        pass


if __name__ == '__main__':
    pass

