import os
import sys
import yaml
import time
import signal
import logging
import tornado.web
import tornado.ioloop
from tornado.options import options, define

import logging
import logging.config

from sqlalchemy import create_engine


logging.config.dictConfig(yaml.load(open('logging.yaml', 'r')))
conf = yaml.load(open('config.yaml', 'r'))

root_path = os.path.dirname(__file__)

settings = {
	"static_path": os.path.join(root_path, "static"),
	"template_path": os.path.join(root_path, "templates"),
	"debug": False,
}


urls = [
		(r'/user','handler.index.UserHandler'),
	]

def get_db_pool():
	dbconf = conf['mysql']
	conn_str = 'mysql://{0}:{1}@{2}:{3}/{4}?charset=utf8'.format(dbconf['user'], dbconf['passwd'], dbconf['host'], dbconf['port'], dbconf['db'])
	engine = create_engine(conn_str, pool_size = dbconf['pool_size'], max_overflow = dbconf['max_overflow'], pool_timeout = dbconf['pool_timeout'])
	return engine

settings['dbpool'] = get_db_pool()
settings['conf'] = conf

def main():
	app = tornado.web.Application(urls, cookie_secret = '0b507c24-0fd9-4adf-87f0-d9d72b229d57', **settings)
	port = conf['server']['port']
	print "Server is starting"
	app.listen(port)

	#Register signal handlers for quittingrole
	signal.signal(signal.SIGTERM, sig_handler)
	signal.signal(signal.SIGINT, sig_handler)

	tornado.ioloop.IOLoop.instance().start()

	logging.info("Exit...")


def sig_handler(sig, frame):
	"""Handles SIGINT by calling shutdown()"""
	logging.warning('Caught signal: %s', sig)
	tornado.ioloop.IOLoop.instance().add_callback(shutdown)


def shutdown():
	"""Waits MAX_WAIT_SECONDS_BEFORE_SHUTDOWN, then shuts down the server"""
	settings['repool'].disconnect()

	MAX_WAIT_SECONDS_BEFORE_SHUTDOWN = 3

	logging.info('Stopping http server')
	# http_server.stop()

	logging.info('Will shutdown in %s seconds ...',
		MAX_WAIT_SECONDS_BEFORE_SHUTDOWN)
	io_loop = tornado.ioloop.IOLoop.instance()

	deadline = time.time() + MAX_WAIT_SECONDS_BEFORE_SHUTDOWN

	def stop_loop():
		now = time.time()
		if now < deadline and (io_loop._callbacks or io_loop._timeouts):
			io_loop.add_timeout(now + 1, stop_loop)
		else:
			io_loop.stop()
		logging.info('Shutdown')

	stop_loop()


if __name__ == '__main__':
 	main()