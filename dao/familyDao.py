from domain.database import DBSession
from domain.family import  Family

# 添加亲情连接
def insertFamily(userId, tel, nickname):
    edFamily = Family(userId=userId, tel=tel, nickname=nickname)
    effect_row = 0
    try:
        session = DBSession()
        session.add(edFamily)
    except Exception:
        session.rollback()
        raise
    else:
        session.commit()
        effect_row = 1
        session.close()
    return effect_row

# 修改亲情连接
def updateFamily(userId, tel, nickname):
    effect_raw = 0
    try:
        session = DBSession()
        family = session.query(Family).filter(Family.userId == userId, Family.tel == tel).first()
        if family is None:
            effect_raw = insertFamily(userId, tel, nickname)
        else:
            family.nickname = nickname
            effect_raw = 1
    except Exception:
        session.rollback()
        raise
    else:
        session.commit()
        session.close()
    return effect_raw

# 通过Id修改亲情连接
def updateFamilyByFamilyId(familyId, userId, tel, nickname):
    effect_raw = 0
    try:
        session = DBSession()
        family = session.query(Family).filter(Family.familyId == familyId, Family.userId == userId).first()
        if family is None:
            effect_raw = 0
        else:
            family.tel = tel
            family.nickname = nickname
            effect_raw = 1
    except Exception:
        session.rollback()
        raise
    else:
        session.commit()
        session.close()
    return effect_raw

# 删除亲情连接
def deleteFamily(familyId, userId):
    effect_raw = 0
    try:
        session = DBSession()
        family = session.query(Family).filter(Family.familyId == familyId, Family.userId == userId).first()
        if family is None:
            effect_raw = 0
        else:
            session.query(Family).filter(Family.familyId == familyId, Family.userId == userId).delete()
            effect_raw = 1
    except Exception:
        session.rollback()
        raise
    else:
        session.commit()
        session.close()
    return effect_raw

# 查看亲情连接列表
def selectFamilyByUserId(userId):
    try:
        session = DBSession()
        family = session.query(Family).filter(Family.userId == userId).all()
        if family is None:
            result = None
        else:
            result = family
    except Exception:
        raise
    else:
        session.close()
        return result

# 某个用户的亲情连接总数
def selectSumFamily(userId):
    try:
        session = DBSession()
        result = session.query(Family).filter(Family.userId == userId).count()
    except Exception:
        raise
    else:
        session.close()
        return result
