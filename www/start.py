#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.web
import tornado.ioloop

class CsrfHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.render('csrf.html')

    def post(self, *args, **kwargs):
        self.write('张岩林已经收到客户端发的请求伪造')

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        if not self.get_secure_cookie("mycookie"):
            self.set_secure_cookie("mycookie","Yes")
            self.write("Your cookie is not set yet")
        else:
            print self.get_secure_cookie("mycookie")
            self.write("Your cookie is right !")


settings = {
    'template_path':'views',
    'static_path':'statics',
    'xsrf_cokkies':True,        # 重点在这里，往这里看
    'cookie_secret': 'helldjkaskak',  # 设定加一段字符串的cookie
}

application = tornado.web.Application([
    (r'/csrf',CsrfHandler),
    (r'/',MainHandler)
],**settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
