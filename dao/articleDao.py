from domain.database import DBSession
from domain.article import Article
import datetime


# 从本地读取文章
def getNewsFromLocal():

    labelOne = '糖尿病新闻'
    labelTwo = ''
    for i in range(1, 101):
        # fileName = r'../article/'+labelOne+'/'+labelTwo+'/'+str(i)+'.txt'
        fileName = r'../article/' + labelOne + '/' + str(i) + '.txt'
        with open(fileName, 'r', encoding='utf-8') as f:
            title = f.readline().split('_')[0]
            con = f.readlines()

        # print(title)
        content = ''
        for j in range(len(con)):
            content = content + con[j]
        imgId = i
        # print(content)
        insertArticle(title, content, labelOne, labelTwo, '', '', '', imgId)


# 添加文章
def insertArticle(title, content, labelOne, labelTwo, labelThree, labelFour, labelFive, imgId):
    session = DBSession()
    articleTime = datetime.datetime.now()
    edArticle = Article(title=title, content=content, articleTime=articleTime, labelOne=labelOne, labelTwo=labelTwo, labelThree=labelThree,labelFour=labelFour, labelFive=labelFive, imgId=imgId, views=0, comNumber=0)
    effect_row = 0
    try:
        session.add(edArticle)
    except Exception:
        session.rollback()
        raise
    else:
        session.commit()
        effect_row = 1
        session.close()
    return effect_row

# 运行主函数
if __name__ == "__main__":
    # getNewsFromLocal()
    pass

# 删除一篇文章
def deleteArticle(articleId):
    try:
        session = DBSession()
        article = session.query(Article).filter(Article.articleId == articleId).first()
        if article is None:
            effect_raw = 0
        else:
            effect_raw = 1
            session.query(Article).filter(Article.articleId == articleId).delete()
    except Exception:
        session.rollback()
        raise
    else:
        session.commit()
        session.close()
    return effect_raw

# 查找一篇文章
def selectArticle(articleId):
    try:
        session = DBSession()
        article = session.query(Article).filter(Article.articleId == articleId).first()
        if article is None:
            result = None
        else:
            result = article
            updateArticleViews(articleId)
    except Exception:
        session.rollback()
        raise
    else:
        session.close()
    return result

# 增加阅读量
def updateArticleViews(articleId):
    try:
        session = DBSession()
        article = session.query(Article).filter(Article.articleId == articleId).first()
        article.views = article.views + 1
    except Exception:
        session.rollback()
        raise
    else:
        session.commit()
        session.close()

# 增加评论数
def updateArticleComNumber(articleId):
    try:
        session = DBSession()
        article = session.query(Article).filter(Article.articleId == articleId).first()
        article.comNumber = article.comNumber + 1
    except Exception:
        session.rollback()
        raise
    else:
        session.commit()
        session.close()

# 修改文章信息
def updateArticle(articleId, title, content, labelOne, labelTwo, labelThree, labelFour, labelFive):
    try:
        session = DBSession()
        article = session.query(Article).filter(Article.articleId == articleId).first()
        if article is None:
            effect_raw = 0
        else:
            effect_raw = 1
            article.title = title
            article.content = content
            article.labelOne = labelOne
            article.labelTwo = labelTwo
            article.labelThree = labelThree
            article.labelFour = labelFour
            article.labelFive = labelFive
    except Exception:
        session.rollback()
        raise
    else:
        session.commit()
        session.close()
    return effect_raw

# 根据文章的articleId返回图片的url
def selectImgUrlByArticleId(aritcileId):
    try:
        session = DBSession()
        aritcile = session.query(Article.labelOne, Article.labelTwo, Article.imgId).filter(Article.articleId == aritcileId).first()
        if aritcile is None:
            result = None
        else:
            result = {'labelOne': aritcile[0], 'labelTwo': aritcile[1], 'imgId': aritcile[2]}
    except Exception:
        raise
    else:
        session.close()
    return result

# 获取最新的n个文章
def selectTopNewestArticle(topN):
    try:
        session = DBSession()
        article = session.query(Article).order_by(Article.articleTime.desc()).limit(topN).all()
        if article is None:
            result = None
        else:
            result = article
    except Exception:
        raise
    else:
        session.close()
        return result

# 从x位置获取后面n篇文章
def selectFromXGetNArticle(x, n):
    try:
        session = DBSession()
        offset = x
        num = x+n
        article = session.query(Article).order_by(Article.articleTime.desc()).slice(offset, num).all()
        if article is None:
            result = None
        else:
            result = article
    except Exception:
        raise
    else:
        session.close()
        return result

# 搜索文章
def selectArticleLikeTitle(labelOne, labelTwo, labelThree, labelFour, labelFive, keyword, x, n):
    try:
        session = DBSession()
        offset = x
        num = x + n
        article = session.query(Article).filter(Article.labelOne.like('%' + labelOne + '%'),
                                                Article.labelTwo.like('%' + labelTwo + '%'),
                                                Article.labelThree.like('%' + labelThree + '%'),
                                                Article.labelFour.like('%' + labelFour + '%'),
                                                Article.labelFive.like('%' + labelFive + '%'),
                                                Article.title.like('%'+keyword+'%')).slice(offset, num).all()
        if article is None:
            result = None
        else:
            result = article
    except Exception:
        raise
    else:
        session.close()
        return result

# 搜索文章总数
def selectSumArticleLikeTitle(labelOne, labelTwo, labelThree, labelFour, labelFive, keyword):
    try:
        session = DBSession()
        result = session.query(Article).filter(Article.labelOne.like('%' + labelOne + '%'),
                                                Article.labelTwo.like('%' + labelTwo + '%'),
                                                Article.labelThree.like('%' + labelThree + '%'),
                                                Article.labelFour.like('%' + labelFour + '%'),
                                                Article.labelFive.like('%' + labelFive + '%'),
                                                Article.title.like('%'+keyword+'%')).count()
    except Exception:
        raise
    else:
        session.close()
        return result

# 查看共有多少篇文章
def selectSumArticle():
    result = 0
    try:
        session = DBSession()
        result = session.query(Article).count()
    except Exception:
        raise
    else:
        session.close()
        return result
