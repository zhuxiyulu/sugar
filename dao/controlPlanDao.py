from domain.database import DBSession
from domain.controlPlan import ControlPlan
import datetime

# 添加控糖方案
def insertControlPlan(userId, min1, max1, min2, max2, sleep1, sleep2):
    controlTime = datetime.datetime.now()
    edControlPlan = ControlPlan(userId=userId, min1=min1, max1=max1,
                                min2=min2, max2=max2, sleep1=sleep1, sleep2=sleep2,
                                controlTime=controlTime)
    effect_row = 0
    try:
        session = DBSession()
        session.add(edControlPlan)
    except Exception:
        session.rollback()
        raise
    else:
        session.commit()
        effect_row = 1
        session.close()
    return effect_row


# 更新控糖方案
def updateControlPlan(userId, min1, max1, min2, max2, sleep1, sleep2):
    try:
        session = DBSession()
        controlPlan = session.query(ControlPlan).filter(ControlPlan.userId == userId).first()
        if controlPlan is None:
            effect_row = insertControlPlan(userId, min1, max1, min2, max2, sleep1, sleep2)
            session.close()
            if effect_row == 1:
                result = 1
            else:
                result = 0
        else:
            controlPlan.min1 = min1
            controlPlan.max1 = max1
            controlPlan.min2 = min2
            controlPlan.max2 = max2
            controlPlan.sleep1 = sleep1
            controlPlan.sleep2 = sleep2
            controlPlan.controlTime = datetime.datetime.now()
            result = 1
    except Exception:
        session.rollback()
        raise
    else:
        session.commit()
        session.close()
    return 1

# 查看控糖方案
def selectConteolPlan(userId):
    try:
        session = DBSession()
        controlPlan = session.query(ControlPlan).filter(ControlPlan.userId == userId).first()
        if controlPlan is None:
            result = None
        else:
            result = controlPlan
    except Exception:
        session.rollback()
        raise
    else:
        session.close()
    return result
