#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import math
from collections import Iterable

# welcome.py

# print "hello world", 'welcome python zoon'


nums = 12 #= int(raw_input('成绩：'))

if not isinstance(nums, (int, float)):
    print '输入的不是有效成绩！'
else:
    if nums >= 60  and nums < 90:
        print '及格'
    elif nums >= 90:
        print '优秀'
    else:
        pass


def my_abs():
    pass


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny


def my_func():
    return None


def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


def add_end(L=[]):
    L.append('END')
    return L


def calc(numbers):
    sum = 0
    for n in numbers:
        sum += n * n
    return sum


def calc01(*numbers):
    sum = 0
    for n in numbers:
        sum += n * n

    return sum


def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw


def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


def filter_prime(v):



my_abs()

a, b = move(100, 100, 60, math.pi / 6)
print a, b

print power(2, 32)

print add_end(), add_end()

print calc([1, 2, 3, 4]), calc((1, 2)), calc01(5, 6, 7)

person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', Job='Engineer')

print fact(10)

print isinstance('abc', Iterable)

print ['/Users/wangxb/github/pythonLab/' + d for d in os.listdir('.')]

L = ['Hello', 'World', 18, 'Apple', None]

print [s.lower() for s in L if isinstance(s, str)]



