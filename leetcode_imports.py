# coding: utf-8
from bisect import *
from builtins import *
from collections import *
from copy import *
from datetime import *
from functools import *
from heapq import *
from io import *
from itertools import *
from json import *
from math import *
from operator import *
from random import *
from re import *
from statistics import *
from string import *
from sys import *
from typing import *


def run(answer, expected):
    if answer != expected:
        raise AssertionError(f"\n\nanswer: {str(answer)}\nexpected: {str(expected)}")
    else:
        print("-------Success!---------------------\n")
