from sqlalchemy import inspect, Column, Integer, SmallInteger, orm,String,Text


from app.models.base import Base


class User(Base):
    openid  = Column(Integer,primary_key=True)
    sessionkey  = Column(String,nullable=False)
    unioid = Column(Integer)
    integrate = Column(Integer,default=0,nullable=False)




