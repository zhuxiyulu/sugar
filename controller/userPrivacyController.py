from dao import userPrivacyDao
from dao.sessionDao import redisCon

# 更新用户隐私设置
def editUserPrivacy(session_id,  isTel, isGender,  isAge, isHeight, isWeight, isArea, isJob, isIntegral):

    if session_id == '':
        data = {'code': 1, 'msg': 'session_id不能为空'}
        return data
    if isTel == '':
        data = {'code': 1, 'msg': '手机设置不能为空'}
        return data
    isTel = int(isTel)
    if isTel != 0 and isTel != 1:
        data = {'code': 1, 'msg': '手机设置有误'}
        return data
    if isGender == '':
        data = {'code': 1, 'msg': '性别设置不能为空'}
        return data
    isGender = int(isGender)
    if isGender != 0 and isGender != 1:
        data = {'code': 1, 'msg': '性别设置有误'}
        return data
    if isAge == '':
        data = {'code': 1, 'msg': '年龄设置不能为空'}
        return data
    isAge = int(isAge)
    if isAge != 0 and isAge != 1:
        data = {'code': 1, 'msg': '年龄设置有误'}
        return data
    if isHeight == '':
        data = {'code': 1, 'msg': '身高设置不能为空'}
        return data
    isHeight = int(isHeight)
    if isHeight != 0 and isHeight != 1:
        data = {'code': 1, 'msg': '身高设置有误'}
        return data
    if isWeight == '':
        data = {'code': 1, 'msg': '体重设置不能为空'}
        return data
    isWeight = int(isWeight)
    if isWeight != 0 and isWeight != 1:
        data = {'code': 1, 'msg': '体重设置有误'}
        return data
    if isArea == '':
        data = {'code': 1, 'msg': '地区设置不能为空'}
        return data
    isArea = int(isArea)
    if isArea != 0 and isArea != 1:
        data = {'code': 1, 'msg': '地区设置有误'}
        return data
    if isJob == '':
        data = {'code': 1, 'msg': '工作设置不能为空'}
        return data
    isJob = int(isJob)
    if isJob != 0 and isJob != 1:
        data = {'code': 1, 'msg': '工作设置有误'}
        return data
    if isIntegral == '':
        data = {'code': 1, 'msg': '经验设置不能为空'}
        return data
    isIntegral = int(isIntegral)
    if isIntegral != 0 and isIntegral != 1:
        data = {'code': 1, 'msg': '经验设置有误'}
        return data
    userId = redisCon.get(session_id)
    if userId is None:
        data = {'code': 1, 'msg': '请先登录'}
        return data
    userId = int(userId)
    effect_raw = userPrivacyDao.updateUserPrivacy(userId, isTel, isGender, isAge, isHeight, isWeight, isArea, isJob, isIntegral)
    if effect_raw == 1:
        data = {'code': 0}
    else:
        data = {'code': 1, 'msg': '隐私权限设置失败'}
    return data

# 查看隐私设置
def retrieveUserPrivacy(session_id):
    if session_id == '':
        data = {'code': 1, 'msg': 'session_id不能为空'}
        return data
    userId = redisCon.get(session_id)
    if userId is None:
        data = {'code': 1, 'msg': '请先登录'}
        return data
    userId = int(userId)
    privacy = userPrivacyDao.selectUserPrivacy(userId)
    if privacy is None:
        data = {'code': 1, 'msg': '无法获取隐私权限'}
    else:
        data = {
            'code': 0,
            'isTel': privacy.isTel,
            'isGender': privacy.isGender,
            'isAge': privacy.isAge,
            'isHeight': privacy.isHeight,
            'isWeight': privacy.isWeight,
            'isArea': privacy.isArea,
            'isJob': privacy.isJob,
            'isIntegral': privacy.isIntegral
        }
    return data