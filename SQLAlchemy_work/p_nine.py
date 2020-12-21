# 连接数据库cookies
from sqlalchemy import create_engine

DB_URI = "mysql+pymysql://root:123456@localhost/cookies"
engine = create_engine(DB_URI, pool_recycle=3600)
connection = engine.connect()

# Example 1-3. More tables with relationships
from sqlalchemy import MetaData
metadata = MetaData()

from sqlalchemy import Table, Column, Integer, Boolean, Numeric  # 有Table就要import Table，Table中有列就要import Colummn，Table中有什么数据类型就要import什么（Integer……）
from sqlalchemy import ForeignKey,ForeignKeyConstraint  # 教学需要，ForeignKey是内敛，ForeignKeyConstraint是显式

orders = Table('orders',metadata,
               Column('order_id', Integer(), primary_key=True),  # 体会ForeignKeyConstraint的显式
               Column('user_id', ForeignKey('users.user_id')),  #找不到users表，应该整合代码片段
               Column('shipped', Boolean(), default=False)
               )

line_items = Table('line_items', metadata,
                   Column('line_items_id', Integer(), primary_key=True),
                   Column('order_id'),  # 体会ForeignKey是内敛
                   Column('cookie_id', ForeignKey('cookies.cookie_id')),
                   Column('quantity', Integer()),
                   Column('extended_cost', Numeric(12, 2))
                   )
ForeignKeyConstraint(['order_id'], ['orders.order_id'])  # Creating the ForeignKeyConstraint for the "order_id" field betweenthe "line_items" and "orders" table

# Persisting the schema to the database
metadata.create_all(engine)  # 不行，必然traceback
