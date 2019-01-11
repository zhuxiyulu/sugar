from sqlalchemy import Column, Integer, String, DATETIME
from domain.database import Base

# SportPlan 运动方案
class SportPlan(Base):
    # 表的名字
    __tablename__ = 'sportplan'

    # 表的结构
    userId = Column(Integer(), primary_key=True)
    sport1 = Column(String())
    sport2 = Column(String())
    sport3 = Column(String())
    sport4 = Column(String())
    time1 = Column(String())
    time2 = Column(String())
    time3 = Column(String())
    time4 = Column(String())
    week1 = Column(String())
    week2 = Column(String())
    week3 = Column(String())
    week4 = Column(String())
    sportTime = Column(DATETIME())

    def __repr__(self):
        return "<SportPlan(userId='%s', sport1='%s', sport2='%s', sport3='%s', sport4='%s', time1='%s', time2='%s', time3='%s', time4='%s', week1='%s', week2='%s', week3='%s',week4='%s', sportTime='%s')>" % (
            self.userIdm,
            self.sport1,
            self.sport2,
            self.sport3,
            self.sport4,
            self.time1,
            self.time2,
            self.time3, 
            self.time4,
            self.week1,
            self.week2,
            self.week3,
            self.week4,
            self.sportTime
        )
