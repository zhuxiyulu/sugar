from dao import replyDao
from dao.sessionDao import redisCon
from dao import usersDao
from dao import topicDao
import uuid
import base64

# 从x位置获取n个跟帖
def retrieveReplyFromXGetN(session_id, topicId, x, n):
    if session_id == '':
        data = {'code': 1, 'msg': 'session_id不能为空'}
        return data
    if topicId == '':
        data = {'code': 1, 'msg': '话题ID不能为空'}
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
    topicId = int(topicId)
    x = int(x)
    n = int(n)
    if x < 0 or n <= 0:
        data = {'code': 1, 'msg': '跟帖获取失败'}
        return data
    result = replyDao.selectReplyFromXGetN(topicId, x, n)
    if result is None:
        data = {'code': 1, 'msg': '跟帖获取失败'}
        return data
    else:
        data = []
        total = replyDao.selectSumReplyByTopicId(topicId)
        for reply in result:
            replyId = reply.replyId
            floor = reply.floor
            userId = reply.userId
            replyTime = reply.replyTime.strftime('%Y-%m-%d %H:%M:%S')
            likes = reply.likes
            comNumber = reply.comNumber
            picture1 = reply.picture1
            picture2 = reply.picture2
            picture3 = reply.picture3
            picture4 = reply.picture4
            picture5 = reply.picture5
            content = reply.content
            user = usersDao.selectUserByUserId(userId)
            if user is None:
                data = {'code': 1, 'msg': '跟帖获取失败'}
                return data
            username = user['username']
            iconUrl = user['iconUrl']

            rep = {'replyId': replyId,
                   'floor': floor,
                   'userId': userId,
                   'username': username,
                   'iconUrl': iconUrl,
                   'replyTime': replyTime,
                   'likes': likes,
                   'picture1': picture1,
                   'picture2': picture2,
                   'picture3': picture3,
                   'picture4': picture4,
                   'picture5': picture5,
                   'comNumber': comNumber,
                   'content': content}
            data.append(rep)
        data = {'code': 0, 'data': data, 'total': total}
    return data

# 添加跟帖的点赞数
def editLikes(session_id, replyId, isLike):
    if session_id == '':
        data = {'code': 1, 'msg': 'session_id不能为空'}
        return data
    if replyId == '':
        data = {'code': 1, 'msg': '跟帖ID不能为空'}
        return data
    if isLike == '':
        data = {'code': 1, 'msg': '点赞数不能为空'}
        return data
    userId = redisCon.get(session_id)
    replyId = int(replyId)
    isLike = int(isLike)
    if isLike != 1 and isLike != -1:
        data = {'code': 1, 'msg': '点赞失败'}
        return data
    if userId is None:
        data = {'code': 1, 'msg': '请先登录'}
        return data
    effect_row = replyDao.updateLikes(replyId, isLike)
    if effect_row == 1:
        data = {'code': 0}
    else:
        data = {'code': 1, 'msg': '点赞失败'}
    return data

# 删除跟帖
def removeReply(session_id, replyId):
    if session_id == '':
        data = {'code': 1, 'msg': 'session_id不能为空'}
        return data
    if replyId == '':
        data = {'code': 1, 'msg': '跟帖ID不能为空'}
        return data
    userId = redisCon.get(session_id)
    if userId is None:
        data = {'code': 1, 'msg': '请先登录'}
        return data
    replyId = int(replyId)
    reply = replyDao.selectReplyByReplyId(replyId)
    topicId = reply.topicId
    result = replyDao.deleteReply(replyId)
    if result == 1:
        # 更新话题中记录的跟帖数量
        topicDao.updateReplyNum(topicId, -1)
        data = {'code': 0, 'msg': '跟帖删除成功'}
    else:
        data = {'code': 1, 'msg': '跟帖无法删除'}
    return data

# 添加跟帖
def createReply(session_id, topicId, content, pictureList):
    if session_id == '':
        data = {'code': 1, 'msg': 'session_id不能为空'}
        return data
    if topicId == '':
        data = {'code': 1, 'msg': '话题ID不能为空'}
        return data
    if content == '':
        data = {'code': 1, 'msg': '跟帖不能为空'}
        return data
    userId = redisCon.get(session_id)
    if userId is None:
        data = {'code': 1, 'msg': '请先登录'}
        return data
    userId = int(userId)
    topicId = int(topicId)
    pictureList = eval(pictureList)
    while len(pictureList) < 5:
        pictureList.append('')
    picture1 = str(pictureList[0])
    picture2 = str(pictureList[1])
    picture3 = str(pictureList[2])
    picture4 = str(pictureList[3])
    picture5 = str(pictureList[4])
    if picture1 != '':
        picture1Url = str(uuid.uuid1())
        fileName = r'templates/static/replyImg/' + picture1Url + '.jpg'
        file = open(fileName, 'wb')
        picture1 = base64.b64decode(picture1)
        file.write(picture1)
        file.close()
        picture1 = '/static/topicImg/' + picture1Url + '.jpg'
    if picture2 != '':
        picture2Url = str(uuid.uuid1())
        fileName = r'templates/static/replyImg/' + picture2Url + '.jpg'
        file = open(fileName, 'wb')
        picture2 = base64.b64decode(picture2)
        file.write(picture2)
        file.close()
        picture2 = '/static/topicImg/' + picture2Url + '.jpg'
    if picture3 != '':
        picture3Url = str(uuid.uuid1())
        fileName = r'templates/static/replyImg/' + picture3Url + '.jpg'
        file = open(fileName, 'wb')
        picture3 = base64.b64decode(picture3)
        file.write(picture3)
        file.close()
        picture3 = '/static/topicImg/' + picture3Url + '.jpg'
    if picture4 != '':
        picture4Url = str(uuid.uuid1())
        fileName = r'templates/static/replyImg/' + picture4Url + '.jpg'
        file = open(fileName, 'wb')
        picture4 = base64.b64decode(picture4)
        file.write(picture4)
        file.close()
        picture4 = '/static/topicImg/' + picture4Url + '.jpg'
    if picture5 != '':
        picture5Url = str(uuid.uuid1())
        fileName = r'templates/static/replyImg/' + picture5Url + '.jpg'
        file = open(fileName, 'wb')
        picture5 = base64.b64decode(picture5)
        file.write(picture5)
        file.close()
        picture5 = '/static/topicImg/' + picture5Url + '.jpg'

    result = replyDao.insertReply(userId, topicId, content, picture1, picture2, picture3, picture4, picture5)
    # 更新跟帖数量
    topicDao.updateReplyNum(topicId, 1)
    # 更新帖子最后回复时间
    topicDao.updateTopicLastTime(topicId)
    if result == 0:
        data = {'code': 1, 'msg': '发表跟帖失败'}
    else:
        data = {'code': 0}
    return data