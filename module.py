#!/usr/bin/env python
# -*- coding:utf-8 -*-

'a test Module by wangxb'

__author__ = 'wangxb'

import sys

try:
    import cStringIO as StringIO
except ImportError:
    import StringIO


def test():
    args = sys.argv
    if len(args) == 1:
        print 'Hello, world'
    elif len(args) == 2:
        print 'Hello, %s' % args[1]
    else:
        print 'Too many arguments!'
    pass


if __name__ == '__main__':
    test()
