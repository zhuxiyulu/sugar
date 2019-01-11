from sqlalchemy import Column, Integer, String, DATE
from domain.database import Base

# Blood 血糖记录
class Blood(Base):
    # 表的名字
    __tablename__ = 'blood'

    # 表的结构
    bloodId = Column(Integer(), primary_key=True, autoincrement=True)
    userId = Column(Integer())
    level = Column(String())
    bloodTime = Column(String())
    bloodDate = Column(DATE)

    def __repr__(self):
        return "<Blood(bloodId='%s', userId='%s', level='%s', ,bloodTime='%s', bloodDate='%s')>" % (
            self.bloodId,
            self.userId,
            self.level,
            self.bloodTime,
            self.bloodDate
        )
