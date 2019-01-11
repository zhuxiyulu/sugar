from dao import familyDao
from dao.sessionDao import redisCon

# 更新亲情连接
def editFamily(session_id, tel, nickname, verifyCode):
    if session_id == '':
        data = {'code': 1, 'msg': 'session_id不能为空'}
        return data
    if tel == '':
        data = {'code': 1, 'msg': '手机号不能为空'}
        return data
    if nickname == '':
        data = {'code': 1, 'msg': '昵称不能为空'}
        return data
    if verifyCode == '':
        data = {'code': 1, 'msg': '验证码不能为空'}
        return data

    userId = redisCon.get(session_id)
    if userId is None:
        data = {'code': 1, 'msg': '请先登录'}
        return data

    telCode = redisCon.get(tel)
    if telCode is None:
        data = {'code': 1, 'msg': '验证码错误或已失效'}
        return data
    if int(telCode) != int(verifyCode):
        data = {'code': 1, 'msg': '无法保存家属链接'}
        return data

    result = familyDao.updateFamily(userId, tel, nickname)
    if result == 0:
        data = {'code': 1, 'msg': '无法保存家属链接'}
    else:
        data = {'code': 0}
    return data

# 获取家属连接列表
def retrieveFamilyList(session_id):
    if session_id == '':
        data = {'code': 1, 'msg': 'session_id不能为空'}
        return data

    userId = redisCon.get(session_id)
    if userId is None:
        data = {'code': 1, 'msg': '请先登录'}
        return data

    familyData = familyDao.selectFamilyByUserId(userId)
    if familyData is None:
        data = {'code': 1, 'msg': '家属连接获取失败'}
    else:
        data = []
        total = familyDao.selectSumFamily(userId)
        for family in familyData:
            familyId = family.familyId
            tel = family.tel
            nickname = family.nickname
            data.append({
                'familyId': familyId,
                'tel': tel,
                'nickname': nickname
            })
        data = {'code': 0, 'data': data, 'total': total}
    return data
