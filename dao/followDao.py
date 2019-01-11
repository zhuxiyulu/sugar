from domain.database import DBSession
from domain.follow import Follow

# 关注
def insertFollow(userId, followId):
    edFollow = Follow(userId=userId, followId=followId)
    effect_row = 0
    try:
        session = DBSession()
        session.add(edFollow)
    except Exception:
        session.rollback()
        raise
    else:
        session.commit()
        session.close()
        effect_row = 1
    return effect_row

# 取消关注
def deleteFollow(userId, followId):
    try:
        session = DBSession()
        follow = session.query(Follow).filter(Follow.userId == userId, Follow.followId == followId).first()
        if follow is None:
            effect_raw = 0
        else:
            effect_raw = 1
            session.query(Follow).filter(Follow.userId == userId, Follow.followId == followId).delete()
    except Exception:
        session.rollback()
        raise
    else:
        session.commit()
        session.close()
    return effect_raw

# 是否关注
def selectFollow(userId, followId):
    try:
        session = DBSession()
        follow = session.query(Follow).filter(Follow.userId == userId, Follow.followId == followId).first()
        if follow is None:
            effect_raw = 0
        else:
            effect_raw = 1
    except Exception:
        session.rollback()
        raise
    else:
        session.close()
    return effect_raw

# 用户查看自己关注的列表
def selectFollowList(userId, x, n):
    try:
        session = DBSession()
        offset = x
        num = x + n
        follow = session.query(Follow).filter(Follow.userId == userId).slice(offset, num).all()
        if follow is None:
            result = None
        else:
            result = follow
    except Exception:
        session.rollback()
        raise
    else:
        session.close()
    return result

# 查看关注我的人
def selectFollowMeList(userId, x, n):
    try:
        session = DBSession()
        offset = x
        num = x + n
        follow = session.query(Follow).filter(Follow.followId == userId).slice(offset, num).all()
        if follow is None:
            result = None
        else:
            result = follow
    except Exception:
        session.rollback()
        raise
    else:
        session.close()
    return result

# 获取用户关注总数
def selectSumFollowByUserId(userId):
    result = 0
    try:
        session = DBSession()
        result = session.query(Follow).filter(Follow.userId == userId).count()
    except Exception:
        raise
    else:
        session.close()
        return result

# 查看用户被关注的总数
def selectSumFollowByFollowId(userId):
    result = 0
    try:
        session = DBSession()
        result = session.query(Follow).filter(Follow.followId == userId).count()
    except Exception:
        raise
    else:
        session.close()
        return result