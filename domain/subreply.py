from sqlalchemy import Column, Integer, String, DATETIME, TEXT
from domain.database import Base

# SubReply跟帖的评论
class SubReply(Base):
    # 表的名字
    __tablename__ = 'subreply'

    # 表的结构
    subreplyId = Column(Integer(), primary_key=True, autoincrement=True)
    content = Column(TEXT())
    subreplyTime = Column(DATETIME())
    replyId = Column(Integer())
    userId = Column(Integer())
    likes = Column(Integer(), default=0)

    def __repr__(self):
        return "<SubReply(subreplyId='%s', content='%s', subreplyTime='%s', replyId='%s', userId='%s', likes='%s')>" % (
            self.subreplyId,
            self.content,
            self.subreplyTime,
            self.replyId,
            self.userId,
            self.likes
        )
