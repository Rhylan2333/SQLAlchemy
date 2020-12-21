# coding: utf-8
from sqlalchemy import create_engine
# 创建实例，并连接blog库
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/blog?charset=utf8')
print(engine)
connection = engine.connect()
