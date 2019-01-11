from domain.database import DBSession
from domain.sportPlan import SportPlan
import datetime

# 添加运动方案
def insertSportPlan(userId, sport1, sport2, sport3, sport4, time1, time2, time3, time4, week1, week2, week3, week4):
    sportTime = datetime.datetime.now()
    edSportPlan = SportPlan(userId=userId, sport1=sport1, sport2=sport2, sport3=sport3, sport4=sport4,
                            time1=time1, time2=time2, time3=time3, time4=time4,
                            week1=week1, week2=week2, week3=week3, week4=week4,
                            sportTime=sportTime
                            )
    effect_row = 0
    try:
        session = DBSession()
        session.add(edSportPlan)
    except Exception:
        session.rollback()
        raise
    else:
        session.commit()
        effect_row = 1
        session.close()
    return effect_row


# 更新运动方案
def updateSportPlan(userId, sport1, sport2, sport3, sport4, time1, time2, time3, time4, week1, week2, week3, week4):
    try:
        session = DBSession()
        sportPlan = session.query(SportPlan).filter(SportPlan.userId == userId).first()
        if sportPlan is None:
            effect_row = insertSportPlan(userId, sport1, sport2, sport3, sport4, time1, time2, time3, time4, week1, week2, week3, week4)
            session.close()
            if effect_row == 1:
                result = 1
            else:
                result = 0
        else:
            sportPlan.sport1 = sport1
            sportPlan.sport2 = sport2
            sportPlan.sport3 = sport3
            sportPlan.sport4 = sport4
            sportPlan.time1 = time1
            sportPlan.time2 = time2
            sportPlan.time3 = time3
            sportPlan.time3 = time4
            sportPlan.week1 = week1
            sportPlan.week2 = week2
            sportPlan.week3 = week3
            sportPlan.week4 = week4
            sportPlan.sportTime = datetime.datetime.now()
            result = 1
    except Exception:
        session.rollback()
        raise
    else:
        session.commit()
        session.close()
    return result

# 查看运动方案
def selectSportPlan(userId):
    try:
        session = DBSession()
        sportPlan = session.query(SportPlan).filter(SportPlan.userId == userId).first()
        if sportPlan is None:
            result = None
        else:
            result = sportPlan
    except Exception:
        session.rollback()
        raise
    else:
        session.close()
    return result
