import json
import time
import urllib
import logging
import tornado.web
from datetime import datetime
from tornado.options import options
from sqlalchemy.orm import scoped_session, sessionmaker


class BaseHandler(tornado.web.RequestHandler):

	def initialize(self):
		super(BaseHandler, self).initialize()

		self.conn = self.conn()
		self.dbsession = self.dbsession()


	def prepare(self):
		self.set_header("Access-Control-Allow-Headers", "x-requested-with")
		self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
		self.add_header("X-Frame-Options", "deny")
		self.add_header("X-XSS-Protection", "1; mode=block")
		self.add_header("X-Content-Type-Options", "nosniff")
		self.add_header("x-ua-compatible:", "IE=edge,chrome=1")
		self.clear_header("Server")

		#if not self._is_pass_outh():
		# 	self._outh()


	def on_finish(self):
		if self.conn:
			self.conn.close()

		if self.dbsession:
			self.dbsession.close()


	def set_default_headers(self):
		pass


	def conn(self):
		dbpool = self.settings['dbpool']
		return dbpool.connect()


	def dbsession(self):
		dbpool = self.settings['dbpool']
		return scoped_session(sessionmaker(bind = dbpool))

	def str2ts(self, s, format):
		dt = datetime.strptime(s, format)
		return int(time.mktime(dt.timetuple()))


	def ts2str(self, ts):
		ts = int(ts)
		return datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')



