# -*- coding:utf-8 -*-
import logging
import json
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

_BaseModel = declarative_base()



class BaseModel(object):
	"""docstring for BaseModel"""
	def __init__(self, **args):
		super(BaseModel, self).__init__()

		self.db = args['conn']


	def select(self, sql):
		ret = self.db.execute(sql)
		if ret.rowcount == 0:
			return []
		return [ dict(zip(i.keys(), i.values())) for i in ret.fetchall() ]

def model_to_dict(insts, cls, columns = None):
	"""
	Jsonify the sql alchemy query result. Skips attr starting with "_"
	"""
	ret = list()
	convert = { "DATETIME": datetime.isoformat}
	
	if isinstance(insts, dict):
		insts = [insts]
		
	for inst in insts:
		d = dict()
		
		for c in cls.__table__.columns:
			if c.name.startswith("_"):
				continue

			if columns and c.name not in columns:
				continue
				
			v = getattr(inst, c.name)
			current_type = str(c.type)
			if current_type in convert.keys() and v is not None:
				try:
					d[c.name] = convert[current_type](v)
				except:
					d[c.name] = "Error:  Failed to covert using ", unicode(convert[c.type])
			elif v is None:
				d[c.name] = unicode()
			else:
				d[c.name] = v
		ret.append(d)
	return ret


model2dict = model_to_dict
