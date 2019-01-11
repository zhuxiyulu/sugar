from domain.database import DBSession
from domain.favoriteArticle import FavoriteArticle

# 收藏文章
def insertFavoriteArticle(userId, articleId):
    edFavorite = FavoriteArticle(userId=userId, articleId=articleId)
    effect_row = 0
    try:
        session = DBSession()
        session.add(edFavorite)
    except Exception:
        session.rollback()
        raise
    else:
        session.commit()
        effect_row = 1
        session.close()
    return effect_row

# 取消收藏的文章
def deleteFavoriteArticle(userId, articleId):
    try:
        session = DBSession()
        article = session.query(FavoriteArticle).filter(FavoriteArticle.userId == userId, FavoriteArticle.articleId == articleId).first()
        if article is None:
            effect_raw = 0
        else:
            effect_raw = 1
            session.query(FavoriteArticle).filter(FavoriteArticle.userId == userId, FavoriteArticle.articleId == articleId).delete()
    except Exception:
        session.rollback()
        raise
    else:
        session.commit()
        session.close()
    return effect_raw

# 根据userId，articleId判断用户是否收藏某篇文章
def seletcFavoriteArticle(userId, articleId):
    effect_raw = 0
    try:
        session = DBSession()
        article = session.query(FavoriteArticle).filter(FavoriteArticle.userId == userId, FavoriteArticle.articleId == articleId).first()
        if article is None:
            effect_raw = 0
        else:
            effect_raw = 1
    except Exception:
        session.rollback()
        raise
    else:
        session.close()
    return effect_raw

# 获取用户收藏的文章
def seletcUserFavoriteArticle(userId, x, n):
    try:
        session = DBSession()
        offset = x
        num = x + n
        article = session.query(FavoriteArticle).filter(FavoriteArticle.userId == userId).slice(offset, num).all()
        if article is None:
            result = None
        else:
            result = article
    except Exception:
        session.rollback()
        raise
    else:
        session.close()
    return result


# 获取用户收藏的文章总数
def selectSumFavoriteArticleByUserId(userId):
    result = 0
    try:
        session = DBSession()
        result = session.query(FavoriteArticle).filter(FavoriteArticle.userId == userId).count()
    except Exception:
        raise
    else:
        session.close()
        return result
