#!/usr/bin/env python
# -*- condig:utf-8 -*-

'class Student'

__author__ = 'wangxb'


class Student(object):

    def __init__(self, name, score, age=20):
        self.__name = name
        self.__score = score
        self._age = age

    def print_score(self):
        print '%s: %s' % (self.__name, self.__score)


a = Student('wangxiaobo', 88)


print a._age, a._Student__name