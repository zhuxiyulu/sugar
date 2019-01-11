from sqlalchemy import Column, Integer
from domain.database import Base

# FavoriteArticle 收藏的文章
class FavoriteArticle(Base):
    # 表的名字
    __tablename__ = 'favoritearticle'

    # 表的结构
    userId = Column(Integer(), primary_key=True)
    articleId = Column(Integer())

    def __repr__(self):
        return "<FavoriteArticle(userId='%s', articleId='%s')>" % (
            self.userId, self.articleId)
