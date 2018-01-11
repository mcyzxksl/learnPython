# -*- coding:utf-8 -*-
import tornado.web
import tornado.ioloop
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index, Sequence
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
from Base import User

engine = create_engine("mysql://root:asdf@127.0.0.1:3306/test")


class UserHandler(tornado.web.RequestHandler):
	def get(self, *args, **kwargs):
		Session = sessionmaker(bind=engine)
		session = Session()
		ret = session.query(User).all()
		session.close()
		self.write(ret)

	def post(self, *args, **kwargs):
		self.write('sadf')


settings = {
    # 'template_path':'views',
		self.write(ret)
    # 'static_path':'statics',
    'xsrf_cokkies':True,
    'cookie_secret': 'helldjkaskak',
}


application = tornado.web.Application([
    (r'/user',UserHandler),
],**settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
