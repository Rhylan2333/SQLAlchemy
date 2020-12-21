# 连接数据库cookies
from sqlalchemy import create_engine

DB_URI = "mysql+pymysql://root:123456@localhost/cookies"
engine = create_engine(DB_URI, pool_recycle=3600)
connection = engine.connect()

# Example 1-2. Another Table with more Column options
from sqlalchemy.dialects.postgresql import JSON

from sqlalchemy import PrimaryKeyConstraint, UniqueConstraint
from sqlalchemy import MetaData
metadata = MetaData()

from datetime import datetime
from sqlalchemy import DateTime

from sqlalchemy import Table, Column, Integer, Numeric, String, ForeignKey  # 感觉ForeignKey多余了，事实上没有，是在为后文接入该表做准备

users = Table('users', metadata,
                Column('user_id', Integer()),
                Column('username', String(15), nullable=False),
                Column('email_address', String(255), nullable=False),
                Column('phone', String(20), nullable=False),
                Column('password', String(25), nullable=False),
                Column('created_on', DateTime(), default=datetime.now),
                Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
                )
# Defining the key explicitly
PrimaryKeyConstraint('user_id', name='user_pk')  # 以下的“name='XX'”看起来像是备注，可不定义name这个参数
UniqueConstraint('username', name='uix_username')

# Persisting the schema to the database
metadata.create_all(engine)
