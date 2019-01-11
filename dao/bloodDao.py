from domain.database import DBSession
from domain.blood import Blood
import json

# 添加血糖记录
def insertGBlood(userId, level, bloodTime, bloodDate):
    edBlood = Blood(userId=userId, level=level, bloodTime=bloodTime, bloodDate=bloodDate)
    effect_row = 0
    try:
        session = DBSession()
        session.add(edBlood)
    except Exception:
        session.rollback()
        raise
    else:
        session.commit()
        effect_row = 1
        session.close()
    return effect_row

# 更新早餐前血糖记录
def updateBloodbeforeBF(userId, bLevel, bTime, bIndex, bloodDate):
    effect_raw = 0
    try:
        session = DBSession()
        blood = session.query(Blood).filter(Blood.userId == userId, Blood.bloodDate == bloodDate).first()
        if blood is None:
            level = {'0': '0', '1': '0', '2': '0', '3': '0', '4': '0', '5': '0', '6': '0'}
            bloodTime = {'0': '0', '1': '0', '2': '0', '3': '0', '4': '0', '5': '0', '6': '0'}
            level[bIndex] = bLevel
            bloodTime[bIndex] = bTime
            effect_raw = insertGBlood(userId, json.dumps(level), json.dumps(bloodTime), bloodDate)
        else:
            level = json.loads(blood.level)
            bloodTime = json.loads(blood.bloodTime)
            level[bIndex] = bLevel
            bloodTime[bIndex] = bTime
            blood.level = json.dumps(level)
            blood.bloodTime = json.dumps(bloodTime)
            effect_raw = 1
    except Exception:
        session.rollback()
        raise
    else:
        session.commit()
        session.close()
    return effect_raw

# 获取用户的血糖记录
def selectUserBloodFromXGetN(userId, x, n):
    try:
        session = DBSession()
        offset = x
        num = x+n
        blood = session.query(Blood).filter(Blood.userId == userId).order_by(Blood.bloodDate.desc()).slice(offset, num).all()
        if blood is None:
            result = None
        else:
            result = blood
    except Exception:
        raise
    else:
        session.close()
        return result

# 某个用户的血糖记录总数
def selectSumBlood(userId):
    try:
        session = DBSession()
        result = session.query(Blood).filter(Blood.userId == userId).count()
    except Exception:
        raise
    else:
        session.close()
        return result

# 精确获取用户某一天血糖记录
def selectUserOneDayBlood(userId, bloodDate):
    try:
        session = DBSession()
        blood = session.query(Blood).filter(Blood.userId == userId, Blood.bloodDate == bloodDate).first()
        if blood is None:
            result = None
        else:
            result = blood
    except Exception:
        raise
    else:
        session.close()
        return result