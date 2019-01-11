from dao import healthDao
from dao.sessionDao import redisCon

# 更新健康记录
def editHealth(session_id, insulin, sportTime, weight, bloodPressure, healthTime, healthDate):
    if session_id == '':
        data = {'code': 1, 'msg': 'session_id不能为空'}
        return data
    if insulin == '':
        data = {'code': 1, 'msg': '胰岛素用量不能为空'}
        return data
    if sportTime == '':
        data = {'code': 1, 'msg': '运动时间不能为空'}
        return data
    if weight == '':
        data = {'code': 1, 'msg': '体重不能为空'}
        return data
    if bloodPressure == '':
        data = {'code': 1, 'msg': '血压不能为空'}
        return data
    if healthTime == '':
        data = {'code': 1, 'msg': '保存时间不能为空'}
        return data
    if healthDate == '':
        data = {'code': 1, 'msg': '日期不能为空'}
        return data
    userId = redisCon.get(session_id)
    if userId is None:
        data = {'code': 1, 'msg': '请先登录'}
        return data

    result = healthDao.updateHealth(userId, insulin, sportTime, weight, bloodPressure, healthTime, healthDate)
    if result == 0:
        data = {'code': 1, 'msg': '无法保存健康记录'}
    else:
        data = {'code': 0}
    return data

# 获取用户健康记录
def retrieveUserHealth(session_id, x, n):
    if session_id == '':
        data = {'code': 1, 'msg': 'session_id不能为空'}
        return data
    if x == '':
        data = {'code': 1, 'msg': 'x不能为空'}
        return data
    if n == '':
        data = {'code': 1, 'msg': 'n不能为空'}
        return data
    x = int(x)
    n = int(n)
    if x < 0 or n <= 0:
        data = {'code': 1, 'msg': '血糖记录获取失败'}
        return data
    userId = redisCon.get(session_id)
    if userId is None:
        data = {'code': 1, 'msg': '请先登录'}
        return data
    healthData = healthDao.selectUserHealthFromXGetN(userId, x, n)
    if healthData is None:
        data = {'code': 1, 'msg': '健康记录获取失败'}
    else:
        data = []
        total = healthDao.selectSumHealth(userId)
        for health in healthData:
            healthId = health.healthId
            insulin = health.insulin
            sportTime = health.sportTime
            weight = health.weight
            bloodPressure = health.bloodPressure
            healthTime = health.healthTime
            healthDate = health.healthDate.strftime('%Y-%m-%d')
            data.append({
                'healthId': healthId,
                'insulin': insulin,
                'sportTime': sportTime,
                'weight': weight,
                'bloodPressure': bloodPressure,
                'healthTime': healthTime,
                'healthDate': healthDate
            })

        data = {'code': 0, 'data': data, 'total': total}
    return data

# 获取用户某一天的健康记录
def retrieveUserOneDayHealth(session_id, healthDate):
    if session_id == '':
        data = {'code': 1, 'msg': 'session_id不能为空'}
        return data
    if healthDate == '':
        data = {'code': 1, 'msg': '日期不能为空'}
        return data

    userId = redisCon.get(session_id)
    if userId is None:
        data = {'code': 1, 'msg': '请先登录'}
        return data
    health = healthDao.selectUserOneDayHealth(userId, healthDate)
    if health is None:
        data = {'code': 1, 'msg': '健康记录获取失败'}
    else:
        data = {
            'code': 0,
            'healthId': health.healthId,
            'insulin': health.insulin,
            'sportTime': health.sportTime,
            'weight': health.weight,
            'bloodPressure': health.bloodPressure,
            'healthTime': health.healthTime
        }
    return data