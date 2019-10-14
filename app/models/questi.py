from sqlalchemy import inspect, Column, Integer, SmallInteger, orm,String

from app.models.base import Base


class Questi(Base):
    id  = Column(Integer,primary_key=True,autoincrement=True)
    question = Column(String(200),unique=True,nullable=False)
    answer = Column(String(200),nullable=False)


    #每个模型要被返回json 请加这个方法 添加字段
    def keys(self):
        return ['question','answer']
