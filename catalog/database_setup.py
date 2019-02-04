import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(270), nullable=False)
    email = Column(String(270), nullable=False)


class dept(Base):
    __tablename__ = 'dept'

    dept_id = Column(Integer, primary_key=True)
    Deptname = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):

        return {
               'dept_id': self.dept_id,
               'Deptname': self.Deptname,
               'user_id': self.user_id,
               }


class students(Base):
    __tablename__ = 'students'

    name = Column(String(80), nullable=False)
    stdid = Column(Integer, primary_key=True)

    dept_id = Column(Integer, ForeignKey('dept.dept_id'))
    dept = relationship(dept)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):

        return {
               'name': self.dept_id,
               'stdid': self.Deptname,
               }

engine = create_engine('sqlite:///dept.db')
Base.metadata.create_all(engine)
