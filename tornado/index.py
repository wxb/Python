#!/usr/bin/env python
# -*- coding:utf-8 -*-


import tornado.ioloop
import tornado.web

'test'

__author__ = 'wangxb'


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


