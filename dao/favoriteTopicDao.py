from domain.database import DBSession
from domain.favoriteTopic import FavoriteTopic

# 收藏话题
def insertFavoriteTopic(userId, topicId):
    edFavorite = FavoriteTopic(userId=userId, topicId=topicId)
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

# 取消收藏的话题
def deleteFavoriteTopic(userId, topicId):
    try:
        session = DBSession()
        topic = session.query(FavoriteTopic).filter(FavoriteTopic.userId == userId, FavoriteTopic.topicId == topicId).first()
        if topic is None:
            effect_raw = 0
        else:
            effect_raw = 1
            session.query(FavoriteTopic).filter(FavoriteTopic.userId == userId, FavoriteTopic.topicId == topicId).delete()
    except Exception:
        session.rollback()
        raise
    else:
        session.commit()
        session.close()
    return effect_raw

# 根据userId，topicId判断用户是否收藏某个话题
def seletcFavoriteTopic(userId, topicId):
    effect_raw = 0
    try:
        session = DBSession()
        topic = session.query(FavoriteTopic).filter(FavoriteTopic.userId == userId, FavoriteTopic.topicId == topicId).first()
        if topic is None:
            effect_raw = 0
        else:
            effect_raw = 1
    except Exception:
        session.rollback()
        raise
    else:
        session.close()
    return effect_raw

# 获取用户收藏的话题
def seletcUserFavoriteTopic(userId, x, n):
    try:
        session = DBSession()
        offset = x
        num = x + n
        topic = session.query(FavoriteTopic).filter(FavoriteTopic.userId == userId).slice(offset, num).all()
        if topic is None:
            result = None
        else:
            result = topic
    except Exception:
        session.rollback()
        raise
    else:
        session.close()
    return result

# 查找某个话题的收藏数
def selectSumTopicByTopicId(topicId):
    try:
        session = DBSession()
        result = session.query(FavoriteTopic).filter(FavoriteTopic.topicId == topicId).count()
    except Exception:
        session.rollback()
        raise
    else:
        session.close()
    return result

# 获取用户收藏的文章总数
def selectSumFavoriteTopicByUserId(userId):
    result = 0
    try:
        session = DBSession()
        result = session.query(FavoriteTopic).filter(FavoriteTopic.userId == userId).count()
    except Exception:
        raise
    else:
        session.close()
        return result