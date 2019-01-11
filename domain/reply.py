from sqlalchemy import Column, Integer, String, DATETIME, TEXT
from domain.database import Base

# Reply跟帖
class Reply(Base):
    # 表的名字
    __tablename__ = 'reply'

    # 表的结构
    replyId = Column(Integer(), primary_key=True, autoincrement=True)
    content = Column(TEXT())
    replyTime = Column(DATETIME())
    userId = Column(Integer())
    topicId = Column(Integer())
    comNumber = Column(Integer())
    floor = Column(Integer())
    likes = Column(Integer(), default=0)
    isRemove = Column(Integer(), default=0)
    picture1 = Column(String())
    picture2 = Column(String())
    picture3 = Column(String())
    picture4 = Column(String())
    picture5 = Column(String())

    def __repr__(self):
        return "<Reply(replyId='%s', content='%s', replyTime='%s', userId='%s', topicId='%s', comNumber='%s', floor='%s', likes='%s', isRemove='%s'), picture1='%s',  picture2='%s',  picture3='%s',  picture4='%s',  picture5='%s'>" % (
            self.replyId,
            self.content,
            self.replyTime,
            self.userId,
            self.topicId,
            self.comNumber,
            self.floor,
            self.likes,
            self.isRemove,
            self.picture1,
            self.picture2,
            self.picture3,
            self.picture4,
            self.picture5
        )
