from sqlalchemy import Column, Integer
from domain.database import Base

# Follow 关注
class Follow(Base):
    # 表的名字
    __tablename__ = 'follow'

    # 表的结构
    # userId 关注 followId
    userId = Column(Integer(), primary_key=True)
    followId = Column(Integer())

    def __repr__(self):
        return "<Follow(userId='%s', followId='%s')>" % (
            self.userId, self.followId)
