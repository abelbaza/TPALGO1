# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 10:45:45 2024

@author: SPECTRE
"""

def binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high)//2
        if target == data[mid]:
            print("target == data[mid], index = mid = ", mid)
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, high)
data = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33]
index = binary_search(data, 17, 0, 28)