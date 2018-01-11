
#-*- coding:utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index, Sequence
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

engine = create_engine("mysql://root:asdf@127.0.0.1:3306/test")

_Base = declarative_base()

class Role(_Base):
	__tablename__ = 'role'

	id = Column(Integer(),autoincrement=True,primary_key=True)
	rolname = Column(String(32))



	
		

class User(_Base):
	__tablename__="user"
	id = Column(Integer,autoincrement=True,primary_key=True)
	name = Column(String(32))
	passwd = Column(String(32))
	age = Column(Integer())
	rid = Column(Integer(),ForeignKey(Role.id))

	def __repr__(self):
		print '<User[name:%s, passwd=%s, age=%d, rid=%d]>' % (self.name,self.passwd,self.age,self.rid)
	

_Base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)
# session = Session()

# session.add_all([
# 	Role(rolname='net'),
# 	Role(rolname='dba')
# ])
# session.commit()
# session.add_all([
# 	User(name='ksl',passwd='asdf',age=27,rid=2)
# ])
# session.commit()
# session.close()

