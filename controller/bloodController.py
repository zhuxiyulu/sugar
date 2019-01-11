from dao import bloodDao
from dao.sessionDao import redisCon
import json

# 更新血糖记录
def editBlood(session_id, period, bLevel, bTime, bloodDate):
    if session_id == '':
        data = {'code': 1, 'msg': 'session_id不能为空'}
        return data
    if period == '':
        data = {'code': 1, 'msg': '时间段不能为空'}
        return data
    if bLevel == '':
        data = {'code': 1, 'msg': '血糖值不能为空'}
        return data
    if bTime == '':
        data = {'code': 1, 'msg': '保存时间不能为空'}
        return data
    if bloodDate == '':
        data = {'code': 1, 'msg': '日期不能为空'}
        return data
    userId = redisCon.get(session_id)
    if userId is None:
        data = {'code': 1, 'msg': '请先登录'}
        return data
    periodList = {
        'beforeBF': '0',
        'afterBF': '1',
        'beforeLC': '2',
        'afterLC': '3',
        'beforeDN': '4',
        'afterDN': '5',
        'beforeSP': '6',
    }
    bIndex = periodList[period]
    result = bloodDao.updateBloodbeforeBF(userId, bLevel, bTime, bIndex, bloodDate)
    if result == 0:
        data = {'code': 1, 'msg': '无法保存血糖记录'}
    else:
        data = {'code': 0}
    return data

# 获取用户血糖记录
def retrieveUserBlood(session_id, x, n):
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
    bloodData = bloodDao.selectUserBloodFromXGetN(userId, x, n)
    if bloodData is None:
        data = {'code': 1, 'msg': '血糖记录获取失败'}
    else:
        data = []
        total = bloodDao.selectSumBlood(userId)
        for blood in bloodData:
            bloodId = blood.bloodId
            level = json.loads(blood.level)
            bloodData = blood.bloodDate.strftime('%Y-%m-%d')
            levelList = [float(v) for v in level.values()]
            averageBlood = '%.2f' % (sum(levelList)/7.0)
            maxBlood = max(levelList)
            minBlood = 1000
            for i in range(len(levelList)):
                if levelList[i] != 0:
                    minBlood = min(minBlood, levelList[i])

            data.append({'bloodId': bloodId,
                         'averageBlood': averageBlood,
                         'maxBlood': maxBlood,
                         'minBlood': minBlood,
                         'bloodDate': bloodData})
        data = {'code': 0, 'data': data, 'total': total}
    return data

# 获取用户某一天的血糖记录
def retrieveUserOneDayBlood(session_id, bloodDate):
    if session_id == '':
        data = {'code': 1, 'msg': 'session_id不能为空'}
        return data
    if bloodDate == '':
        data = {'code': 1, 'msg': '日期不能为空'}
        return data

    userId = redisCon.get(session_id)
    if userId is None:
        data = {'code': 1, 'msg': '请先登录'}
        return data
    blood = bloodDao.selectUserOneDayBlood(userId, bloodDate)
    if blood is None:
        data = {'code': 1, 'msg': '血糖记录获取失败'}
    else:
        data = {'code': 0, 'bloodId': blood.bloodId, 'level': json.loads(blood.level), 'bloodTime': json.loads(blood.bloodTime)}
    return data