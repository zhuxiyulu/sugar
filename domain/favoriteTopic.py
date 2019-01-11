from sqlalchemy import Column, Integer
from domain.database import Base

# FavoriteTopic 收藏的话题
class FavoriteTopic(Base):
    # 表的名字
    __tablename__ = 'favoritetopic'

    # 表的结构
    userId = Column(Integer(), primary_key=True)
    topicId = Column(Integer())

    def __repr__(self):
        return "<FavoriteTopic(userId='%s', topicId='%s')>" % (
            self.userId, self.topicId)
