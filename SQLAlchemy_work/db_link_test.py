from sqlalchemy import create_engine
# encoding: utf-8

# 可读性高的代码
# HOSTNAME = "127.0.0.1"
# PORT = "3306"
# DATABASE = "cookies"
# USERNAME = "root"
# PASSWORD = "123456"
# DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}".\
#    format(username=USERNAME, password=PASSWORD, host=HOSTNAME, port=PORT, db=DATABASE)

# 简化的代码
DB_URI = "mysql+pymysql://root:123456@localhost/cookies"

engine = create_engine(DB_URI, pool_recycle=3600)

connection = engine.connect()
# 测试部分
result = connection.execute("select 1")
print(result.fetchone())
