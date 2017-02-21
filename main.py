# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Date  : 2017-02-21
# Author: juzi
# E-mail: jentlewoo@gmail.com


import tornado.ioloop
import tornado.web
from handlers import *

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

