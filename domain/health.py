from sqlalchemy import Column, Integer, String, DATE
from domain.database import Base

# Health 健康记录
class Health(Base):
    # 表的名字
    __tablename__ = 'health'

    # 表的结构
    healthId = Column(Integer(), primary_key=True, autoincrement=True)
    userId = Column(Integer())
    insulin = Column(String())   # 胰岛素用量
    sportTime = Column(String())  # 运动时长
    weight = Column(String())  # 体重
    bloodPressure = Column(String())  # 血压
    healthTime = Column(String())  # 保存记录的时间
    healthDate = Column(DATE())  # 保存记录的日期

    def __repr__(self):
        return "<Health(healthId='%s', userId='%s', insulin='%s', sportTime='%s', weight='%s', bloodPressure='%s', heightTime='%s', healthDate='%s')>" % (
            self.healthId,
            self.userId,
            self.insulin,
            self.sportTime,
            self.weight,
            self.bloodPressure,
            self.healthTime,
            self.healthDate
        )
