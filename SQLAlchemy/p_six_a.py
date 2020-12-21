# 连接数据库cookies
from sqlalchemy import create_engine

DB_URI = "mysql+pymysql://root:123456@localhost/cookies"
engine = create_engine(DB_URI, pool_recycle=3600)
connection = engine.connect()

# Example 1-1. Instantiating Table objects and columns
from sqlalchemy.dialects.postgresql import JSON

from sqlalchemy import MetaData
metadata = MetaData()

from sqlalchemy import Table, Column, Integer, Numeric, String, ForeignKey
from sqlalchemy import CheckConstraint, Index

cookies = Table('cookies', metadata,
                Column('cookie_id', Integer(), primary_key=True),
                Column('cookie_name', String(50), index=True),
                Column('cookie_recipe_url', String(255)),
                Column('cookie_sku', String(55)),
                Column('quantity', Integer()),
                Column('unit_cost', Numeric(12, 2))
                )
# Defining the key explicitly
CheckConstraint('unit_cost >= 0.00', name='unit_cost_positive')
# Defining an index using an explicit construction type
Index('ix_cookies_cookie_name', 'cookie_name')
# If we want to select by "cookie_SKU" and "cookie_name"
Index('ix_test', cookies.c.cookie_sku, cookies.c.cookie_name)
# Persisting the schema to the database
metadata.create_all(engine)
