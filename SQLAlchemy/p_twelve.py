# 连接数据库cookies
from sqlalchemy import create_engine

DB_URI = "mysql+pymysql://root:123456@localhost/cookies"
engine = create_engine(DB_URI, pool_recycle=3600)
connection = engine.connect()  # 可以不要这个行代码

from sqlalchemy import MetaData
metadata = MetaData()
from datetime import datetime
from sqlalchemy import Table, Column, Integer, String, Numeric
from sqlalchemy import CheckConstraint, Index, insert

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

# Example 2-1. Single insert as a method
ins = cookies.insert().values(
    cookie_name="chocolate chip",
    cookie_recipe_url="http://some.aweso.me/cookie/recipe.html",
    cookie_sku="CC01",
    quantity="12",
    unit_cost="0.50"
    )
# print(str(ins))
print(ins.compile().params)  # Returning a SQLCompiler object that will be sent with the query via the params attribute

result = connection.execute(ins)  # Executing the insert statement
print(result.inserted_primary_key)  # Get the ID of the record we just inserted by accessing the inserted_primary_key attribute

# Example 2-3. Insert function
ins = insert(cookies).values(
    cookie_name="chocolate chip",
    cookie_recipe_url="http://some.aweso.me/cookie/recipe.html",
    cookie_sku="CC01",
    quantity="12",
    unit_cost="0.50"
    )
print(ins.compile().params)  # Returning a SQLCompiler object that will be sent with the query via the params attribute

result = connection.execute(ins)  # Executing the insert statement
print(result.inserted_primary_key)  # Get the ID of the record we just inserted by accessing the inserted_primary_key attribute

# Example 2-4. Values in execute statement
ins = cookies.insert()
result = connection.execute(
    ins,
    cookie_name='dark chocolate chip',
    cookie_recipe_url='http://some.aweso.me/cookie/recipe_dark.html',
    cookie_sku='CC02',
    quantity='1',
    unit_cost='0.75'
    )
print(ins.compile().params)  # Returning a SQLCompiler object that will be sent with the query via the params attribute
print(result.inserted_primary_key)  # Get the ID of the record we just inserted by accessing the inserted_primary_key attribute

# Example 2-5. Multiple inserts
inventory_list = [
    {
        'cookie_name': 'peanut butter',
        'cookie_recipe_url': 'http://some.aweso.me/cookie/peanut.html',
        'cookie_sku': 'PB01',
        'quantity': '24',
        'unit_cost': '0.25'
        },
    {
        'cookie_name': 'oatmeal raisin',
        'cookie_recipe_url': 'http://some.okay.me/cookie/raisin.html',
        'cookie_sku': 'EWW01',
        'quantity': '100',
        'unit_cost': '1.00'
        }
    ]
print(ins.compile().params)  # Returning a SQLCompiler object that will be sent with the query via the params attribute

result = connection.execute(ins, inventory_list)
# print(result.inserted_primary_key)  # 这里不能用是因为插入了多条记录
