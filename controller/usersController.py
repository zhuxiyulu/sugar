from dao import usersDao
from dao import userPrivacyDao
from dao.sessionDao import redisCon
from dao import followDao
import uuid
import datetime

# 用户登录验证
def userLoginVerify(tel, password):
    if tel == '':
        data = {'code': 1, 'msg': '手机号码不能为空'}
        return data
    if password == '':
        data = {'code': 1, 'msg': '密码不能为空'}
        return data

    userData = usersDao.selectUserByTel(tel)
    if userData is None:
        data = {'code': 1, 'msg': '用户名或密码错误'}
    else:
        tablePassword = userData.password
        if tablePassword != password:
            data = {'code': 1, 'msg': '用户名或密码错误'}
        else:
            userId = userData.userId
            session_id = str(uuid.uuid3(uuid.NAMESPACE_DNS, str(userId)))
            exTime = int(7*24*60*60)
            try:
                redisCon.set(session_id, userId, ex=exTime)
                redisCon.set(userId, session_id, ex=exTime)
            except Exception:
                data = {'code': 1, 'msg': '登录失败'}
                return data
            username = userData.username
            iconUrl = userData.iconUrl
            integral = userData.integral
            chectTime = userData.checkTime.strftime('%Y-%m-%d %H:%M:%S')
            nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            d1 = datetime.datetime.strptime(chectTime, '%Y-%m-%d %H:%M:%S')
            d2 = datetime.datetime.strptime(nowTime, '%Y-%m-%d %H:%M:%S')
            delta = d2 - d1
            if delta.days < 1:
                isCheck = 1
            else:
                isCheck = 0

            data = {'code': 0,
                    'userId': userId,
                    'session_id': session_id,
                    'username': username,
                    'iconUrl': iconUrl,
                    'integral': integral,
                    'isCheck': isCheck
                    }

    return data

# 登出
def userLogout(session_id):
    if session_id == '':
        data = {'code': 1, 'msg': 'session_id不能为空'}
        return data
    userId = redisCon.get(session_id)
    if userId is None:
        data = {'code': 1, 'msg': '无法登出'}
    else:
        redisCon.delete(userId)
        redisCon.delete(session_id)
        data = {'code': 0}
    return data


# 通过session_id获取用户个人信息
def retrieveUserBySessionId(session_id):
    if session_id == '':
        data = {'code': 1, 'msg': 'session_id不能为空'}
        return data
    try:
        userId = redisCon.get(session_id)
        result = usersDao.selectUserByUserId(userId)
    except Exception:
        data = {'code': 1, 'msg': '用户信息获取失败'}
        return data
    if userId is None:
        data = {'code': 1, 'msg': '请先登录'}
        return data
    if result is None:
        data = {'code': 1, 'msg': '用户信息获取失败'}
    else:
        data = {'code': 0,
                'tel': result['tel'],
                'username': result['username'],
                'gender': result['gender'],
                'age': result['age'],
                'height': result['height'],
                'weight': result['weight'],
                'area': result['area'],
                'job': result['job'],
                'iconUrl': result['iconUrl'],
                'integral': result['integral']
                }
    return data

# 通过session_id，otherUserId获取其他用户信息
def retrieveOtherUserInfoByUserId(session_id, otherUserId):
    if session_id == '':
        data = {'code': 1, 'msg': 'session_id不能为空'}
        return data
    if otherUserId == '':
        data = {'code': 1, 'msg': 'otherUserId不能为空'}
        return data
    userId = redisCon.get(session_id)
    if userId is None:
        data = {'code': 1, 'msg': '请先登录'}
        return data
    result = usersDao.selectUserByUserId(otherUserId)
    if result is None:
        data = {'code': 1, 'msg': '用户信息获取失败'}
    else:
        isFollow = followDao.selectFollow(int(userId), int(otherUserId))
        userPrivacy = userPrivacyDao.selectUserPrivacy(int(otherUserId))
        if userPrivacy.isTel == 1:
            tel = result['tel']
        else:
            tel = ''
        if userPrivacy.isGender == 1:
            gender = result['gender']
        else:
            gender = ''
        if userPrivacy.isAge == 1:
            age = result['age']
        else:
            age = ''
        if userPrivacy.isHeight == 1:
            height = result['height']
        else:
            height = ''
        if userPrivacy.isWeight == 1:
            weight = result['weight']
        else:
            weight = ''
        if userPrivacy.isArea == 1:
            area = result['area']
        else:
            area = ''
        if userPrivacy.isJob == 1:
            job = result['job']
        else:
            job = ''
        if userPrivacy.isIntegral == 1:
            integral = result['integral']
        else:
            integral = ''

        data = {'code': 0,
                'tel': tel,
                'username': result['username'],
                'gender': gender,
                'age': age,
                'height': height,
                'weight': weight,
                'area': area,
                'job': job,
                'iconUrl': result['iconUrl'],
                'integral': integral,
                'isFollow': isFollow
                }
    return data

# 用户注册
def createUser(tel, username, verifyCode, password):
    if tel == '':
        data = {'code': 1, 'msg': '手机号不能为空'}
        return data
    if username == '':
        data = {'code': 1, 'msg': '用户名不能为空'}
        return data
    if verifyCode == '':
        data = {'code': 1, 'msg': '验证码不能为空'}
        return data
    if password == '':
        data = {'code': 1, 'msg': '密码不能为空'}
        return data

    tableCode = redisCon.get(tel)
    if tableCode is None:
        data = {'code': 1, 'msg': '验证码错误或已失效'}
        return data
    if int(tableCode) == int(verifyCode):
        result = usersDao.insertUser(tel, password, username)
        if result == 0:
            userData = usersDao.selectUserByTel(tel)
            userId = userData.userId
            effect_raw = userPrivacyDao.insertUserPrivacy(userId)
            if effect_raw == 1:
                data = {'code': 0}
            else:
                data = {'code': 1, 'msg': '注册失败'}
        elif result == 2:
            data = {'code': 1, 'msg': '该用户已经注册'}
        else:
            data = {'code': 1, 'msg': '注册失败'}
    else:
        data = {'code': 1, 'msg': '验证码错误或已失效'}
    return data

# 修改一个用户信息
def editUser(session_id, username, gender, age, heigth, weight, area, job):
    if session_id == '':
        data = {'code': 1, 'msg': 'session_id不能为空'}
        return data
    if username == '':
        data = {'code': 1, 'msg': 'username不能为空'}
        return data
    userId = redisCon.get(session_id)
    if userId is None:
        data = {'code': 1, 'msg': '请先登录'}
        return data
    age = int(age)
    if age <= 0 or age >= 200:
        data = {'code': 1, 'msg': '年龄有误'}
        return data

    result = usersDao.updateUser(userId, username, gender, age, heigth, weight, area, job)
    if result == 0:
        data = {'code': 1, 'msg': '暂时无法修改'}
    else:
        data = {'code': 0}
    return data

# 更新用户积分
def editUserIntegral(session_id, integral):
    if session_id == '':
        data = {'code': 1, 'msg': 'session_id不能为空'}
        return data
    if integral == '':
        data = {'code': 1, 'msg': '积分不能为空'}
        return data
    userId = redisCon.get(session_id)
    if userId is None:
        data = {'code': 1, 'msg': '请先登录'}
        return data
    integral = int(integral)
    result = usersDao.updateUserIntegral(userId, integral)
    if result == 1:
        data = {'code': 0}
    else:
        data = {'code': 1, 'msg': '经验更新失败'}
    return data

# 删除一个用户
def removeUser(session_id, userId):
    if session_id == '':
        data = {'code': 1, 'msg': 'session_id不能为空'}
        return data
    user = redisCon.get(session_id)
    if user is None:
        data = {'code': 1, 'msg': '请先登录'}
        return data
    userId = int(userId)
    result = usersDao.deleteUser(userId)
    if result == 1:
        data = {'code': 0, 'msg': '用户删除成功'}
    else:
        data = {'code': 1, 'msg': '用户删除失败'}
    return data

# 从x位置获取后面n个用户
def getFromXGetNUser(x, n):
    if x == '':
        data = {'code': 1, 'msg': 'x不能为空'}
        return data
    if n == '':
        data = {'code': 1, 'msg': 'n不能为空'}
        return data
    x = int(x)
    n = int(n)
    if x < 0 or n <= 0:
        data = {'code': 1, 'msg': '无法获取用户'}
        return data
    result = usersDao.selectFromXGetNUser(x, n)
    if result is None:
        data = {'code': 1, 'msg': '无法获取x之后n个用户'}
    else:
        data = []
        total = usersDao.selectSumUsers()
        for user in result:
            tel = user.tel
            username = user.username
            gender = user.gender
            age = user.age
            signTime = user.signTime.strftime('%Y-%m-%d %H:%M:%S')
            height = user.height
            weight = user.weight
            area = user.area
            job = user.job
            integral = user.integral
            users = {'tel': tel,
                     'username': username,
                     'gender': gender,
                     'age': age,
                     'signTime': signTime,
                     'height': height,
                     'weight': weight,
                     'area': area,
                     'job': job,
                     'integral': integral
                     }
            data.append(users)
        data = {'code': 0, 'data': data, 'total': total}
    return data

# 修改密码
def editUserPassword(tel, verifyCode, password):
    if tel == '':
        data = {'code': 1, 'msg': '手机号不能为空'}
        return data
    if verifyCode == '':
        data = {'code': 1, 'msg': '验证码不能为空'}
        return data
    if password == '':
        data = {'code': 1, 'msg': '密码不能为空'}
        return data
    tableCode = redisCon.get(tel)
    if tableCode is None:
        data = {'code': 1, 'msg': '验证码错误或已失效'}
        return data
    if int(tableCode) == int(verifyCode):
        effect_raw = usersDao.updateUserPassword(tel, password)
        if effect_raw == 1:
            data = {'code': 0}
        else:
            data = {'code': 1, 'msg': '密码修改失败'}
    else:
        data = {'code': 1, 'msg': '验证码错误或已失效'}
    return data

# 用户签到
def editUserCheckTime(session_id):
    if session_id == '':
        data = {'code': 1, 'msg': 'session_id不能为空'}
        return data
    userId = redisCon.get(session_id)
    if userId is None:
        data = {'code': 1, 'msg': '请先登录'}
        return data
    userId = int(userId)
    result = usersDao.updateCheckTime(userId)
    if result == 1:
        data = {'code': 0}
    else:
        data = {'code': 1, 'msg': '签到失败'}
    return data

# 管理员界面从x位置获取后面n个用户
def adminGetFromXGetNUser(session_id, x, n):
    if session_id == '':
        data = {'code': 1, 'msg': 'session_id不能为空'}
        return data
    if x == '':
        data = {'code': 1, 'msg': 'x不能为空'}
        return data
    if n == '':
        data = {'code': 1, 'msg': 'n不能为空'}
        return data
    userId = redisCon.get(session_id)
    if userId is None:
        data = {'code': 1, 'msg': '请先登录'}
        return data
    x = int(x)
    n = int(n)
    if x < 0 or n <= 0:
        data = {'code': 1, 'msg': '无法获取用户'}
        return data
    result = usersDao.selectFromXGetNUser(x, n)
    if result is None:
        data = {'code': 1, 'msg': '无法获取x之后n个用户'}
        return data
    else:
        data = []
        total = usersDao.selectSumUsers()
        for user in result:
            userId = user.userId
            tel = user.tel
            username = user.username
            gender = user.gender
            age = user.age
            signTime = user.signTime.strftime('%Y-%m-%d %H:%M:%S')
            height = user.height
            weight = user.weight
            area = user.area
            job = user.job
            integral = user.integral
            users = {'userId': userId,
                     'tel': tel,
                     'username': username,
                     'gender': gender,
                     'age': age,
                     'signTime': signTime,
                     'height': height,
                     'weight': weight,
                     'area': area,
                     'job': job,
                     'integral': integral
                     }
            data.append(users)
        temp = {'total': total, 'rows': data, 'code': 0}
        return temp
