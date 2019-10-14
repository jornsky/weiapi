from sqlalchemy import  Column, Integer, String


from app.models.base import Base


class Askanswer(Base):
    id  = Column(Integer,primary_key=True,autoincrement=True)
    mail = Column(String(40),nullable=False)
    subject = Column(String(20),nullable=False)
    cate = Column(String(20),nullable=False)




