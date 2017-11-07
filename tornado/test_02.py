#!/usr/bin/env python
# -*- coding:utf-8 -*-


import tornado.ioloop
import tornado.web

'test 02'

__author__ = 'wangxb'


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write('<html><body><form action="/" method="post">'
                   '<input type="text" name="message">'
                   '<input type="submit" value="Submit">'
                   '</form></body></html>')

    def post(self):
        print self._get_argument()
        if not self.get_argument('message'):
            raise tornado.web.HTTPError(403)
        else:
            self.set_header("Content-Type", "text/plain")
            self.write("You wrote " + self.get_argument("message"))


class StoryHandle(tornado.web.RequestHandler):
    def get(self, sid):
        self.write("You requested the story " + sid)

    def post(self, *args, **kwargs):
        pass


app = tornado.web.Application([
    (r'/', MainHandler),
    (r'/story/([0-9]+)', StoryHandle)
])


if __name__ == '__main__':
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

