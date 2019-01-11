from domain.database import DBSession
from domain.users import User
import datetime
import random

# 通过userId获取用户个人信息
def selectUserByUserId(userId):
    try:
        session = DBSession()
        user = session.query(User).filter(User.userId == userId).first()
        if user is None:
            result = None
        else:
            result = {'tel': user.tel,
                      'username': user.username,
                      'gender': user.gender,
                      'age': user.age,
                      'height': user.height,
                      'weight': user.weight,
                      'area': user.area,
                      'job': user.job,
                      'iconUrl': user.iconUrl,
                      'integral': user.integral,
                      }

    except Exception:
        raise
    else:
        session.close()
    return result

# 通过tel获取用户个人信息
def selectUserByTel(tel):
    try:
        session = DBSession()
        user = session.query(User).filter(User.tel == tel).first()
        if user is None:
            result = None
        else:
            result = user
    except Exception:
        raise
    else:
        session.close()
    return result


# 用户注册
def insertUser(tel, password, username):
    result = 1
    try:
        if selectUserByTel(tel) is None:
            session = DBSession()
            signTime = datetime.datetime.now()
            iconUrl = '/static/userImg/usertile' + str(random.randint(10, 44)) + '.jpg'
            edUser = User(tel=tel, password=password, username=username, signTime=signTime, iconUrl=iconUrl, checkTime=signTime)
            session.add(edUser)
        else:
            result = 2
            return result
    except Exception:
        session.rollback()
        raise
    else:
        session.commit()
        result = 0
        session.close()
    return result

# 修改一个用户信息
def updateUser(userId, username, gender, age, height, weight, area, job):

    try:
        session = DBSession()
        user = session.query(User).filter(User.userId == userId).first()
        if user is None:
            effect_raw = 0
        else:
            effect_raw = 1
            user.username = username
            user.gender = gender
            user.age = age
            user.height = height
            user.weight = weight
            user.area = area
            user.job = job
        '''
        session.query(User).filter(User.userId == userId).update(
            {
                User.username: username,
                User.gender: gender,
                User.age: age
            }, synchronize_session=False)
        '''
    except Exception:
        session.rollback()
        raise
    else:
        session.commit()
        session.close()
    return effect_raw

# 更新用户积分
def updateUserIntegral(userId, integral):
    try:
        session = DBSession()
        user = session.query(User).filter(User.userId == userId).first()
        if user is None:
            effect_raw = 0
        else:
            effect_raw = 1
            user.integral = user.integral + integral
    except Exception:
        session.rollback()
        raise
    else:
        session.commit()
        session.close()
    return effect_raw

# 删除一个用户
def deleteUser(userId):
    try:
        session = DBSession()
        user = session.query(User).filter(User.userId == userId).first()
        if user is None:
            effect_raw = 0
        else:
            effect_raw = 1
            session.query(User).filter(User.userId == userId).delete()
    except Exception:
        session.rollback()
        raise
    else:

        session.commit()
        session.close()
    return effect_raw

# 从x位置获取后面n个用户
def selectFromXGetNUser(x, n):
    try:
        session = DBSession()
        offset = x
        num = x + n
        user = session.query(User).slice(offset, num).all()
    except Exception:
        raise
    else:
        session.close()
        return user

# 修改密码
def updateUserPassword(tel, password):
    try:
        session = DBSession()
        user = session.query(User).filter(User.tel == tel).first()
        if user is None:
            effect_raw = 0
        else:
            effect_raw = 1
            user.password = password
    except Exception:
        session.rollback()
        raise
    else:
        session.commit()
        session.close()
    return effect_raw

# 查看共有多少个用户
def selectSumUsers():
    result = 0
    try:
        session = DBSession()
        result = session.query(User).count()
    except Exception:
        raise
    else:
        session.close()
        return result


# 用户签到
def updateCheckTime(userId):
    checkTime = datetime.datetime.now()
    try:
        session = DBSession()
        user = session.query(User).filter(User.userId == userId).first()
        if user is None:
            effect_raw = 0
        else:
            effect_raw = 1
            user.checkTime = checkTime
    except Exception:
        session.rollback()
        raise
    else:
        session.commit()
        session.close()
    return effect_raw