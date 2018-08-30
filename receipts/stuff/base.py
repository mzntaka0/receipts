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

class CreateText(metaclass=ABCMeta):

    @abstractmethod
    def __call__(self):
        pass



if __name__ == '__main__':
    pass

