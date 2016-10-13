# -*- coding: utf-8 -*-
from random import randint
from sys import argv

try:
    k = int(argv[1])
    s = int(argv[2])
except:
    k = 10
    s = 1

a = [randint(1, 100) for x in range(k)]


def insertion_sort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i -= 1
        a[i + 1] = key
    return a

if s == 1:
    print(a)
    print("="*(k*4))
    print(insertion_sort(a))
else:
    insertion_sort(a)
