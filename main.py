# -*- coding: utf-8 -*-
def is_monotonic(array):
    if array == sorted(array) or array == sorted(array, reverse=True):
        return True
    else:
        return False
"""
Created on Wed Nov 10 23:06:11 2021

@author: anast
"""

