# -*- coding: utf-8 -*-
from random import randint
from sys import argv
try:
    k = int(argv[1])
    s = int(argv[2])
except:
    k = 10
    s = 1

a = [randint(1,100) for x in range(k)]

def merge(left, right):
    l = len(left)
    r = len(right)
    n = l + r
    i = 0
    j = 0
    result = []
    for k in range(n):
        if i < l and (j == r or left[i] <= right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    return result

def merge_sort(a):
    n = len(a)
    if n <= 1:
        return a
    q = n // 2
    left = merge_sort(a[:q])
    right = merge_sort(a[q:])
    return merge(left, right)

if s == 1:
    print(a)
    print(merge_sort(a))
else:
    merge_sort(a)