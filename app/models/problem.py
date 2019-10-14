from sqlalchemy import inspect, Column, Integer, SmallInteger, orm,String,Text


from app.models.base import Base


class Problem(Base):
    id  = Column(Integer,primary_key=True,autoincrement=True)
    ques = Column(String(200),nullable=False)





