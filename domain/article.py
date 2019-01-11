from sqlalchemy import Column, Integer, String, TEXT, DateTime
from domain.database import Base

# Article 文章
class Article(Base):
    # 表的名字
    __tablename__ = 'article'

    # 表的结构
    articleId = Column(Integer(), primary_key=True, autoincrement=True)
    title = Column(String())
    content = Column(TEXT())
    articleTime = Column(DateTime())
    labelOne = Column(String())
    labelTwo = Column(String())
    labelThree = Column(String())
    labelFour = Column(String())
    labelFive = Column(String())
    imgId = Column(Integer())
    views = Column(Integer(), default=0)
    comNumber = Column(Integer(), default=0)
    
    def __repr__(self):
        return "<Article(articleId='%s', title='%s', content='%s', articleTime='%s', labelOne='%s', labelTwo='%s', labelThree='%s', labelFour='%s', labelFive='%s', imgId='%s', views='%s', comNumber='%s')>" % (
            self.articleId, self.title, self.content, self.articleTime, self.labelOne, self.labelTwo, self.labelThree, self.labelFour, self.labelFive, self.imgId, self.views, self.comNumber)
