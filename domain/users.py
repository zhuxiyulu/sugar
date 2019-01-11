from sqlalchemy import Column, Integer, String, DECIMAL, DATETIME
from domain.database import Base

# User 用户
class User(Base):
    # 表的名字
    __tablename__ = 'users'

    # 表的结构
    userId = Column(Integer(), primary_key=True, autoincrement=True)
    tel = Column(String(30))
    password = Column(String())
    username = Column(String(30))
    gender = Column(String(2))
    age = Column(Integer())
    signTime = Column(DATETIME())
    height = Column(DECIMAL())
    weight = Column(DECIMAL())
    area = Column(String())
    job = Column(String())
    integral = Column(Integer())
    iconUrl = Column(String())
    checkTime = Column(DATETIME())

    def __repr__(self):
        return "<User(userId='%s', tel='%s', password='%s', username='%s' gender='%s' age='%s' signTime='%s height='%s', weight='%s', area='%s', job='%s', integral='%s'), iconUrl='%s', checkTime='%s'>" % (
            self.userId, self.tel, self.password, self.username, self.gender, self.age,
            self.signTime, self.height, self.weight, self.area, self.job, self.integral,
            self.iconUrl, self.checkTime)
