from sqlalchemy import Column, Integer, String, DateTime
from domain.database import Base

# 控糖方案 饮食方案
class ControlPlan(Base):
    # 表的名字
    __tablename__ = 'controlplan'

    # 表的结构
    userId = Column(Integer(), primary_key=True)
    min1 = Column(String())
    max1 = Column(String())
    min2 = Column(String())
    max2 = Column(String())
    sleep1 = Column(String())
    sleep2 = Column(String())
    controlTime = Column(DateTime())

    def __repr__(self):
        return "<ControlPlan(userId='%s', min1='%s', max1='%s', min2='%s', max2='%s', sleep1='%s', sleep2='%s', controlTime='%s')>" % (
            self.userId,
            self.min1,
            self.max1,
            self.min2,
            self.max2,
            self.sleep1,
            self.sleep2,
            self.controlTime
            )
