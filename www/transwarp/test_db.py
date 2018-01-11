#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, create_engine,Integer,Sequence,ForeignKey
from sqlalchemy.orm import sessionmaker,aliased,relationship
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(Integer, Sequence('user_id_seq'),primary_key=True)
    name = Column(String(20))
    passwd = Column(String(20))
    age = Column(Integer)

    def __repr__(self):
    	return "<User(id='%s',name='%s',passwd='%s',age='%s')>" % (self.id,self.name,self.passwd,self.age)

class School(Base):
    # 表的名字:
    __tablename__ = 'school'

    # 表的结构:
    id = Column(Integer, Sequence('user_id_seq'),primary_key=True)
    name = Column(String(20))
    uid = Column(String(20))
    claNum = Column(Integer)

    def __repr__(self):
    	return "<School(id='%s',name='%s',claNum)='%s'>" % (self.id,self.name,self.claNum)

class Address(Base):
	__tablename__ = 'address'
	id= Column(Integer,Sequence('user_id_seq'),primary_key=True)
	email_address = Column(String(20),nullable=False)
	user_id = Column(Integer,ForeignKey('user.id'))

	user = relationship("User",back_populates="address")

	def __repr__(self):
		return "<Address(email_address='%s')>" % self.email_address
User.address=relationship("Address",order_by=Address.id,back_populates="user")



# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:asdf@localhost:3306/test')
# 初始化数据库表
Base.metadata.create_all(engine)


# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
session = DBSession()
new_user = User(name='Bob1',age=17,passwd="asdf")
new_user.address=[Address(email_address="mcyzxksl1@163.com"),Address(email_address="keshilin1@ane56.com")]
session.add(new_user)

# new_user.age=22
# session.commit()
Query.join(User.address)
for u in session.query(User).join(Address).filter(Address.email_address=="mcyzxksl@163.com").all():
	print u
	# print u.address
# for u in session.query.join(User.address).all():
# 	print u
	# print a
# for our_user, in session.query(User.id).filter(User.name=="bob").all():
# 	print our_user
# for age in session.query(User.age).filter_by(name='bob'):
# 	print age

#类别名
# usertest1 = aliased(User,name='usertest')
# for row in session.query(usertest1,usertest1.name).all():
# 	print (row.usertest)

#user1 = session.query(User).filter(User.id=='5').one()
# 打印类型和对象的name属性:
#print user1
# 关闭Session:
session.close()