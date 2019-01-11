from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 创建对象的基类:
Base = declarative_base()

# create_engine方法，创建数据库链接，
# create_engine方法参数('使用数据库+数据库链接模块://数据库用户名:密码@ip地址:端口/要连接的数据库名称',echo=True表示是否查看生成的sql语句)
engine = create_engine('mysql+pymysql://@127.0.0.1:3306/?charset=utf8', echo=False)

# Base.metadata.create_all(engine)  # 向数据库创建指定表，如果表存在忽略创建

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)