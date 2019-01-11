from sqlalchemy import Column, Integer, TEXT, ForeignKey, String, DateTime
from domain.database import Base

# Comment 评论
class Comment(Base):
    # 表的名字
    __tablename__ = 'comment'

    # 表的结构
    commentId = Column(Integer(), primary_key=True, autoincrement=True)
    content = Column(TEXT())
    commentTime = Column(DateTime())
    userId = Column(Integer())
    articleId = Column(Integer())
    likes = Column(Integer(), default=0)

    def __repr__(self):
        return "<Comment(commentId='%s', content='%s', commentTime='%s', userId='%s', articleId='%s')>" % (
            self.commentId, self.content, self.commentTime, self.userId, self.articleId)
