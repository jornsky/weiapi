from sqlalchemy import inspect, Column, Integer, SmallInteger, orm,String,Text


from app.models.base import Base


class Subject(Base):
    id  = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(200),unique=True,nullable=False)
    content = Column(Text,nullable=False)
    cate = Column(String(20),nullable=False)
    views = Column(Integer,nullable=True,default=0)




    def keys(self):
        return  ['id','title','content','cate','views']

    def get_top(self,number):
        #降序排列
        re_list = Subject.query.order_by(Subject.views.desc()).limit(number).all()
        return  re_list






