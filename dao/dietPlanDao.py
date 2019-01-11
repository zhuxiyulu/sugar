from domain.database import DBSession
from domain.dietPlan import DietPlan
import datetime

# 添加饮食方案
def insertDietPlan(userId, change, cereals, fruit, meat, milk, fat, vegetables):
    dietTime = datetime.datetime.now()
    edDeitPlan = DietPlan(userId=userId, change=change, cereals=cereals, fruit=fruit,
                          meat=meat, milk=milk, fat=fat, vegetables=vegetables, dietTime=dietTime)
    effect_row = 0
    try:
        session = DBSession()
        session.add(edDeitPlan)
    except Exception:
        session.rollback()
        raise
    else:
        session.commit()
        effect_row = 1
        session.close()
    return effect_row


# 更新饮食方案
def updateDietPlan(userId, change, cereals, fruit, meat, milk, fat, vegetables):
    try:
        session = DBSession()
        dietPlan = session.query(DietPlan).filter(DietPlan.userId == userId).first()
        if dietPlan is None:
            effect_row = insertDietPlan(userId, change, cereals, fruit, meat, milk, fat, vegetables)
            if effect_row == 1:
                result = 1
            else:
                result = 0
        else:
            dietPlan.change = change
            dietPlan.cereals = cereals
            dietPlan.fruit = fruit
            dietPlan.meat = meat
            dietPlan.milk = milk
            dietPlan.fat = fat
            dietPlan.vegetables = vegetables
            dietPlan.dietTime = datetime.datetime.now()
            result = 1
    except Exception:
        session.rollback()
        raise
    else:
        session.commit()
        session.close()
    return result

# 查看饮食方案
def selectDietPlan(userId):
    try:
        session = DBSession()
        dietPlan = session.query(DietPlan).filter(DietPlan.userId == userId).first()
        if dietPlan is None:
            result = None
        else:
            result = dietPlan
    except Exception:
        session.rollback()
        raise
    else:
        session.close()
    return result
