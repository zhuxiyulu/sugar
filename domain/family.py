from sqlalchemy import Column, Integer, String
from domain.database import Base

# Family 亲情连接
class Family(Base):
    # 表的名字
    __tablename__ = 'family'

    # 表的结构
    familyId = Column(Integer(), primary_key=True, autoincrement=True)
    userId = Column(Integer())
    tel = Column(String())
    nickname = Column(String())

    def __repr__(self):
        return "<Family(familyId='%s', userId='%s', tel='%s', nickname='%s')>" % (
            self.familyId,
            self.userId,
            self.tel,
            self.nickname
        )
