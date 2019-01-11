from dao import followDao
from dao import usersDao
from dao.sessionDao import redisCon

# 关注
def createFollow(session_id, followId):
    if session_id == '':
        data = {'code': 1, 'msg': 'session_id不能为空'}
        return data
    if followId == '':
        data = {'code': 1, 'msg': 'followId不能为空'}
        return data
    userId = redisCon.get(session_id)
    if userId is None:
        data = {'code': 1, 'msg': '请先登录'}
        return data

    userId = int(userId)
    followId = int(followId)
    effect_row = followDao.insertFollow(userId, followId)
    if effect_row == 1:
        data = {'code': 0}
    else:
        data = {'code': 1, 'msg': '无法关注'}
    return data

# 取消关注
def removeFollow(session_id, followId):
    if session_id == '':
        data = {'code': 1, 'msg': 'session_id不能为空'}
        return data
    if followId == '':
        data = {'code': 1, 'msg': 'followId不能为空'}
        return data
    userId = redisCon.get(session_id)
    if userId is None:
        data = {'code': 1, 'msg': '请先登录'}
        return data

    userId = int(userId)
    followId = int(followId)
    effect_row = followDao.deleteFollow(userId, followId)
    if effect_row == 1:
        data = {'code': 0}
    else:
        data = {'code': 1, 'msg': '无法取消关注'}
    return data

# 用户查看自己关注的列表
def retrieveFollowList(session_id, x, n):
    if session_id == '':
        data = {'code': 1, 'msg': 'session_id不能为空'}
        return data
    userId = redisCon.get(session_id)
    if userId is None:
        data = {'code': 1, 'msg': '请先登录'}
        return data

    userId = int(userId)
    x = int(x)
    n = int(n)
    if x < 0 or n <= 0:
        data = {'code': 1, 'msg': '关注获取失败'}
        return data
    result = followDao.selectFollowList(userId, x, n)
    if result is None:
        data = {'code': 1, 'msg': '请先登录'}
    else:
        data = []
        total = followDao.selectSumFollowByUserId(userId)
        for follow in result:
            followId = follow.followId
            userData = usersDao.selectUserByUserId(int(followId))
            fol = {'followId ': followId, 'username': userData['username'], 'iconUrl': userData['iconUrl']}
            data.append(fol)
        data = {'code': 0, 'data': data, 'total': total}
    return data

# 查看关注我的人
def retrieveFollowMeList(session_id, x, n):
    if session_id == '':
        data = {'code': 1, 'msg': 'session_id不能为空'}
        return data
    userId = redisCon.get(session_id)
    if userId is None:
        data = {'code': 1, 'msg': '请先登录'}
        return data

    userId = int(userId)
    x = int(x)
    n = int(n)
    if x < 0 or n <= 0:
        data = {'code': 1, 'msg': '关注获取失败'}
        return data
    result = followDao.selectFollowMeList(userId, x, n)
    if result is None:
        data = {'code': 1, 'msg': '请先登录'}
    else:
        data = []
        total = followDao.selectSumFollowByFollowId(userId)
        for followMe in result:
            followMeId = followMe.userId
            userData = usersDao.selectUserByUserId(int(followMeId))
            fol = {'followMeId ': followMeId, 'username': userData['username'], 'iconUrl': userData['iconUrl']}
            data.append(fol)
        data = {'code': 0, 'data': data, 'total': total}
    return data