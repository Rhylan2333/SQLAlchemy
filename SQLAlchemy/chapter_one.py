# 连接数据库cookies
from sqlalchemy import create_engine

DB_URI = "mysql+pymysql://root:123456@localhost/cookies"
engine = create_engine(DB_URI, pool_recycle=3600)
connection = engine.connect()  # 可以不要这个行代码

from sqlalchemy import MetaData
metadata = MetaData()
from datetime import datetime
from sqlalchemy import Table, Column, Integer, Numeric, String, Boolean, DateTime, ForeignKey
from sqlalchemy import CheckConstraint, Index, PrimaryKeyConstraint, UniqueConstraint, ForeignKeyConstraint

cookies = Table('cookies', metadata,
                Column('cookie_id', Integer(), primary_key=True),
                Column('cookie_name', String(50)),  # “, index=True”可被加进去，内敛的index
                Column('cookie_recipe_url', String(255)),
                Column('cookie_sku', String(55)),
                Column('quantity', Integer()),
                Column('unit_cost', Numeric(12, 2))
                )
CheckConstraint('unit_cost >= 0.00', name='unit_cost_positive')  # Defining the key explicitly
Index('ix_cookies_cookie_name', 'cookie_name')  # Defining an index using an explicit construction type
Index('ix_test', cookies.c.cookie_sku, cookies.c.cookie_name)  # If we want to select by "cookie_SKU" and "cookie_name"

users = Table('users', metadata,
                Column('user_id', Integer()),
                Column('username', String(15), nullable=False),  # Column('username', String(15), nullable=False, unique=True),内敛的unique
                Column('email_address', String(255), nullable=False),
                Column('phone', String(20), nullable=False),
                Column('password', String(25), nullable=False),
                Column('created_on', DateTime(), default=datetime.now),
                Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
                )
PrimaryKeyConstraint('user_id', name='user_pk')  # 以下的“name='XX'”看起来像是备注，可不定义name这个参数
UniqueConstraint('username', name='uix_username')  # Defining the key explicitly

orders = Table('orders',metadata,
               Column('order_id', Integer(), primary_key=True),
               Column('user_id', ForeignKey('users.user_id')),  # users表在上面  # 体会ForeignKeyConstraint的显式
               Column('shipped', Boolean(), default=False)
               )

line_items = Table('line_items', metadata,
                   Column('line_items_id', Integer(), primary_key=True),
                   Column('order_id'),
                   Column('cookie_id', ForeignKey('cookies.cookie_id')),  # 体会ForeignKey是内敛
                   Column('quantity', Integer()),
                   Column('extended_cost', Numeric(12, 2))
                   )
ForeignKeyConstraint(['order_id'], ['orders.order_id'])  # Creating the ForeignKeyConstraint for the "order_id" field betweenthe "line_items" and "orders" table
# Persisting the schema to the database(cookies)
metadata.create_all(engine)
