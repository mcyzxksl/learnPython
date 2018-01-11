#-*- coding:utf-8 -*-
import json
import tornado.web
import tornado.ioloop
from base import BaseHandler
from model.People import UserModel
from model.Base import model2dict


class UserHandler(BaseHandler):
	def initialize(self):
		super(UserHandler, self).initialize()

	def get(self):
		user = self.dbsession.query(UserModel).all()
		print user
		self.write( json.dumps(model2dict(user,UserModel)))
		# self.write(json.dumps(user))
