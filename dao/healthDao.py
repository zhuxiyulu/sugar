from domain.database import DBSession
from domain.health import Health

# 保存每日健康记录
def insertHealth(userId, insulin, sportTime, weight, bloodPressure, healthTime, healthDate):
    edHealth = Health(userId=userId,
                      insulin=insulin,
                      sportTime=sportTime,
                      weight=weight,
                      bloodPressure=bloodPressure,
                      healthTime=healthTime,
                      healthDate=healthDate)
    effect_row = 0
    try:
        session = DBSession()
        session.add(edHealth)
    except Exception:
        session.rollback()
        raise
    else:
        session.commit()
        effect_row = 1
        session.close()
    return effect_row

# 更新健康记录
def updateHealth(userId, insulin, sportTime, weight, bloodPressure, healthTime, healthDate):
    effect_raw = 0
    try:
        session = DBSession()
        health = session.query(Health).filter(Health.userId == userId, Health.healthDate == healthDate).first()
        if health is None:
            effect_raw = insertHealth(userId, insulin, sportTime, weight, bloodPressure, healthTime, healthDate)
        else:
            health.insulin = insulin
            health.sportTime = sportTime
            health.weight = weight
            health.bloodPressure = bloodPressure
            health.healthTime = healthTime
            effect_raw = 1
    except Exception:
        session.rollback()
        raise
    else:
        session.commit()
        session.close()
    return effect_raw

# 查询用户的健康记录
def selectUserHealthFromXGetN(userId, x, n):
    try:
        session = DBSession()
        offset = x
        num = x+n
        health = session.query(Health).filter(Health.userId == userId).order_by(Health.healthDate.desc()).slice(offset, num).all()
        if health is None:
            result = None
        else:
            result = health
    except Exception:
        raise
    else:
        session.close()
        return result

# 某个用户的健康记录总数
def selectSumHealth(userId):
    try:
        session = DBSession()
        result = session.query(Health).filter(Health.userId == userId).count()
    except Exception:
        raise
    else:
        session.close()
        return result

# 精确获取用户某一天健康记录
def selectUserOneDayHealth(userId, healthDate):
    try:
        session = DBSession()
        health = session.query(Health).filter(Health.userId == userId, Health.healthDate == healthDate).first()
        if health is None:
            result = None
        else:
            result = health
    except Exception:
        raise
    else:
        session.close()
        return result