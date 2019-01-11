from sqlalchemy import Column, Integer
from domain.database import Base

# UserPrivacy 信息是否显示给其他用户
class UserPrivacy(Base):
    # 表的名字
    __tablename__ = 'userprivacy'

    # 表的结构
    # 1 表示显示（默认）
    userId = Column(Integer(), primary_key=True)
    isTel = Column(Integer(), default=1)
    isGender = Column(Integer(), default=1)
    isAge = Column(Integer(), default=1)
    isHeight = Column(Integer(), default=1)
    isWeight = Column(Integer(), default=1)
    isArea = Column(Integer(), default=1)
    isJob = Column(Integer(), default=1)
    isIntegral = Column(Integer(), default=1)

    def __repr__(self):
        return "<UserPrivacy(userId='%s',  isTel='%s', isGender='%s',  isAge='%s', isHeight='%s',  isWeight='%s', isArea='%s', isJob='%s', isIntegral='%s')>" % (
            self.userId,
            self.isTel,
            self.isGender,
            self.isAge,
            self.isHeight,
            self.isWeight,
            self.isArea,
            self.isJob,
            self.isIntegral
        )
