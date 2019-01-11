from domain.userPrivacy import UserPrivacy
from domain.database import DBSession

# 增加用户隐私设置
def insertUserPrivacy(userId):
    adUserPrivacy = UserPrivacy(userId=userId, isTel=1, isGender=1, isAge=1, isHeight=1, isWeight=1, isArea=1, isJob=1, isIntegral=1)
    effect_raw = 0
    try:
        session =DBSession()
        session.add(adUserPrivacy)
    except Exception:
        session.rollback()
        raise
    else:
        effect_raw = 1
        session.commit()
        session.close()
    return effect_raw

# 更新用户隐私设置
def updateUserPrivacy(userId, isTel, isGender, isAge, isHeight, isWeight, isArea, isJob, isIntegral):
    try:
        session = DBSession()
        userPrivacy = session.query(UserPrivacy).filter(UserPrivacy.userId == userId).first()
        if userPrivacy is None:
            effect_raw = 0
        else:
            userPrivacy.isTel = isTel
            userPrivacy.isGender = isGender
            userPrivacy.isAge = isAge
            userPrivacy.isHeight = isHeight
            userPrivacy.isWeight = isWeight
            userPrivacy.isArea = isArea
            userPrivacy.isJob = isJob
            userPrivacy.isIntegral = isIntegral
            effect_raw = 1
    except Exception:
        session.rollback()
        raise
    else:
        session.commit()
        session.close()
    return effect_raw

# 查询用户隐私设置
def selectUserPrivacy(userId):
    try:
        session = DBSession()
        userPrivacy = session.query(UserPrivacy).filter(UserPrivacy.userId == userId).first()
        if userPrivacy is None:
            result = None
        else:
            result = userPrivacy
    except Exception:
        session.rollback()
        raise
    else:
        session.close()
    return result
