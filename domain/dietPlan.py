from sqlalchemy import Column, Integer, String, DateTime
from domain.database import Base

# DietPlan 饮食方案
class DietPlan(Base):
    # 表的名字
    __tablename__ = 'dietplan'

    # 表的结构
    userId = Column(Integer(), primary_key=True)
    change = Column(String())  # 交换
    cereals = Column(String())  # 谷物
    fruit = Column(String())
    meat = Column(String())
    milk = Column(String())
    fat = Column(String())
    vegetables = Column(String())
    dietTime = Column(DateTime())
    def __repr__(self):
        return "<DietPlan(userId='%s', change='%s', cereals='%s', fruit='%s', meat='%s', milk='%s', fat='%s', vegetables='%s', dietTime='%s')>" % (
            self.userId, self.change, self.cereals, self.fruit, self.meat, self.milk, self.fat, self.vegetables, self.dietTime)
