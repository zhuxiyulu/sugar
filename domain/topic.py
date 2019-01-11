from sqlalchemy import Column, Integer, String, DATETIME, TEXT
from domain.database import Base

# Topic 话题
class Topic(Base):
    # 表的名字
    __tablename__ = 'topic'

    # 表的结构
    topicId = Column(Integer(), primary_key=True, autoincrement=True)
    content = Column(TEXT())
    topicTime = Column(DATETIME())
    userId = Column(Integer())
    lastTime = Column(DATETIME())
    picture1 = Column(String())
    picture2 = Column(String())
    picture3 = Column(String())
    picture4 = Column(String())
    picture5 = Column(String())
    likes = Column(Integer(), default=0)
    replyNum = Column(Integer(), default=0)
    comNum = Column(Integer(), default=0)

    def __repr__(self):
        return "<Topic(topicId='%s', content='%s', topicTime='%s', userId='%s', lastTime='%s', picture1='%s', picture2='%s', picture3='%s', picture4='%s', picture5='%s', likes='%s', replyNum='%s', comNum='%s')>" % (
            self.topicId,
            self.content,
            self.topicTime,
            self.userId,
            self.lastTime,
            self.picture1,
            self.picture2,
            self.picture3,
            self.picture4,
            self.picture5,
            self.likes,
            self.replyNum,
            self.comNum
        )
