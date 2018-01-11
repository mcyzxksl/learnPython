

import json
import logging
import time
from sqlalchemy import Column, Integer, String ,ForeignKey
from sqlalchemy.orm import relationship
from Base import _BaseModel


class Role(_BaseModel):
	__tablename__ = 'role'

	id = Column(Integer(),autoincrement=True,primary_key=True)
	rolname = Column(String(32))
	# user = relationship("UserModel",back_populates="role")

	# def __repr__(self):
	# 	return 'Role[id:%d, rolname=%s' % (self.id, self.rolname)



	
		

class UserModel(_BaseModel):
	__tablename__="user"
	id = Column(Integer,autoincrement=True,primary_key=True)
	name = Column(String(32))
	passwd = Column(String(32))
	age = Column(Integer())
	rid = Column(Integer(),ForeignKey(Role.id))
	# role = relationship("Role",back_populates="user")	

	def __repr__(self):
		return 'name:%s, passwd=%s, age=%d, rid=%d' % (self.name,self.passwd,self.age,self.rid)

	
