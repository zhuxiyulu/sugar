from dao import topicDao
from dao.sessionDao import redisCon
from dao import usersDao
from dao import favoriteTopicDao
from dao import replyDao
from dao import subReplyDao
import uuid
import base64

# 获取最新话题列表
def retrieveLastTopicList(session_id, topicIdList, n):
    if session_id == '':
        data = {'code': 1, 'msg': 'session_id不能为空'}
        return data
    if topicIdList == '':
        data = {'code': 1, 'msg': '已有话题列表不能为空'}
        return data
    if n == '':
        data = {'code': 1, 'msg': 'n不能为空'}
        return data
    userId = redisCon.get(session_id)
    if userId is None:
        data = {'code': 1, 'msg': '请先登录'}
        return data
    n = int(n)
    if n <= 0:
        data = {'code': 1, 'msg': '话题获取失败'}
        return data
    topicIdList = eval(topicIdList)
    result = topicDao.selectLastTopicList(topicIdList, n)
    if result is None:
        data = {'code': 1, 'msg': '话题获取失败'}
        return data
    else:
        data = []
        for topic in result:
            topicId = topic.topicId
            userId = topic.userId
            lastTime = topic.lastTime.strftime('%Y-%m-%d %H:%M:%S')
            content = topic.content[:40]
            picture1 = topic.picture1
            picture2 = topic.picture2
            picture3 = topic.picture3
            replyNum = topic.replyNum
            comNum = topic.comNum
            user = usersDao.selectUserByUserId(userId)
            if user is None:
                data = {'code': 1, 'msg': '话题获取失败'}
                return data
            username = user['username']
            iconUrl = user['iconUrl']

            top = {'topicId': topicId,
                   'userId': userId,
                   'username': username,
                   'iconUrl': iconUrl,
                   'lastTime': lastTime,
                   'content': content,
                   'picture1': picture1,
                   'picture2': picture2,
                   'picture3': picture3,
                   'replyNum': replyNum,
                   'comNum': comNum}
            data.append(top)
        data = {'code': 0, 'data': data}
    return data

# 添加话题的点赞数
def editLikes(session_id, topicId, likes):
    if session_id == '':
        data = {'code': 1, 'msg': 'session_id不能为空'}
        return data
    if topicId == '':
        data = {'code': 1, 'msg': '话题ID不能为空'}
        return data
    if likes == '':
        data = {'code': 1, 'msg': '点赞数不能为空'}
        return data
    userId = redisCon.get(session_id)
    topicId = int(topicId)
    likes = int(likes)
    if likes != 1 and likes != -1:
        data = {'code': 1, 'msg': '点赞失败'}
        return data
    if userId is None:
        data = {'code': 1, 'msg': '请先登录'}
        return data
    effect_row = topicDao.updateLikes(topicId, likes)
    if effect_row == 1:
        data = {'code': 0}
    else:
        data = {'code': 1, 'msg': '点赞失败'}
    return data

# 获取用户发布的话题
def retrieveTopicByUserId(session_id, x, n):
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
        data = {'code': 1, 'msg': '获取话题失败'}
        return data
    topicData = topicDao.selectFromXGetNTopicByUserId(userId, x, n)
    if topicData is None:
        data = {'code': 1, 'msg': '获取话题失败'}
    else:
        data = []
        total = topicDao.selectSumTopicByUserId(userId)
        for topic in topicData:
            topicId = topic.topicId
            content = topic.content[:40]
            picture1 = topic.picture1
            picture2 = topic.picture2
            picture3 = topic.picture3
            replyNum = topic.replyNum
            comNum = topic.comNum
            likes = topic.likes
            topicTime = topic.topicTime.strftime('%Y-%m-%d %H:%M:%S')
            favoriteNum = favoriteTopicDao.selectSumTopicByTopicId(topicId)

            top = {'topicId': topicId,
                   'content': content,
                   'picture1': picture1,
                   'picture2': picture2,
                   'picture3': picture3,
                   'replyNum': replyNum,
                   'comNum': comNum,
                   'likes': likes,
                   'topicTime': topicTime,
                   'favoriteNum': favoriteNum
                   }
            data.append(top)
        data = {'code': 0, 'data': data}
    return data

# 根据话题ID获取话题
def retrieveTopicByTopicId(session_id, topicId):
    if session_id == '':
        data = {'code': 1, 'msg': 'session_id不能为空'}
        return data
    if topicId == '':
        data = {'code': 1, 'msg': 'topicId不能为空'}
        return data
    userId = redisCon.get(session_id)
    if userId is None:
        data = {'code': 1, 'msg': '请先登录'}
        return data

    userId = int(userId)
    topicId = int(topicId)
    topic = topicDao.selectTopicByTopicId(topicId)
    if topic is None:
        data = {'code': 1, 'msg': '获取话题失败'}
    else:
        topicTime = topic.topicTime.strftime('%Y-%m-%d %H:%M:%S')
        likes = topic.likes
        content = topic.content
        picture1 = topic.picture1
        picture2 = topic.picture2
        picture3 = topic.picture3
        picture4 = topic.picture4
        picture5 = topic.picture5
        favorite = favoriteTopicDao.seletcFavoriteTopic(userId, topicId)
        topicUserId = topic.userId
        user = usersDao.selectUserByUserId(topicUserId)
        if user is None:
            data = {'code': 1, 'msg': '话题获取失败'}
            return data
        username = user['username']
        iconUrl = user['iconUrl']
        top = {'userId': topicUserId,
               'username': username,
               'iconUrl': iconUrl,
               'topicTime': topicTime,
               'favorite': favorite,
               'likes': likes,
               'content': content,
               'picture1': picture1,
               'picture2': picture2,
               'picture3': picture3,
               'picture4': picture4,
               'picture5': picture5,
               }
        data = {'code': 0, 'data': top}
    return data

# 搜索话题
def retrieveTopicLikeTopic(session_id, keyword, x, n):
    if session_id == '':
        data = {'code': 1, 'msg': 'session_id不能为空'}
        return data
    if keyword == '':
        data = {'code': 1, 'msg': '关键词不能为空'}
        return data
    if x == '':
        data = {'code': 1, 'msg': '起始位置不能为空'}
        return data
    if n == '':
        data = {'code': 1, 'msg': '文章数量不能为空'}
        return data
    userId = redisCon.get(session_id)
    if userId is None:
        data = {'code': 1, 'msg': '请先登录'}
        return data
    x = int(x)
    n = int(n)
    if n <= 0 or x < 0:
        data = {'code': 1, 'msg': '搜索失败'}
        return data
    result = topicDao.selectTopicLikeContent(keyword, x, n)
    if result is None:
        data = {'code': 1, 'msg': '无法搜索文章'}
    else:
        data = []
        total = topicDao.selectSumTopicLikeContent(keyword)
        for topic in result:
            topicId = topic.topicId
            lastTime = topic.lastTime.strftime('%Y-%m-%d %H:%M:%S')
            content = topic.content[:40]
            userId = topic.userId
            user = usersDao.selectUserByUserId(userId)
            if user is None:
                data = {'code': 1, 'msg': '话题获取失败'}
                return data
            username = user['username']
            iconUrl = user['iconUrl']
            top = {'topicId': topicId,
                   'lastTime': lastTime,
                   'content': content,
                   'userId': userId,
                   'username': username,
                   'iconUrl': iconUrl
                   }
            data.append(top)
        data = {'code': 0, 'data': data, 'total': total}
    return data

# 新建话题
def createTopic(session_id, content, pictureList):
    if session_id == '':
        data = {'code': 1, 'msg': 'session_id不能为空'}
        return data
    if content == '':
        data = {'code': 1, 'msg': '话题不能为空'}
        return data
    userId = redisCon.get(session_id)
    if userId is None:
        data = {'code': 1, 'msg': '请先登录'}
        return data
    userId = int(userId)
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
        fileName = r'templates/static/topicImg/' + picture1Url + '.jpg'
        file = open(fileName, 'wb')
        picture1 = base64.b64decode(picture1)
        file.write(picture1)
        file.close()
        picture1 = '/static/topicImg/' + picture1Url + '.jpg'
    if picture2 != '':
        picture2Url =str(uuid.uuid1())
        fileName = r'templates/static/topicImg/' + picture2Url + '.jpg'
        file = open(fileName, 'wb')
        picture2 = base64.b64decode(picture2)
        file.write(picture2)
        file.close()
        picture2 = '/static/topicImg/' + picture2Url + '.jpg'
    if picture3 != '':
        picture3Url = str(uuid.uuid1())
        fileName = r'templates/static/topicImg/' + picture3Url + '.jpg'
        file = open(fileName, 'wb')
        picture3 = base64.b64decode(picture3)
        file.write(picture3)
        file.close()
        picture3 = '/static/topicImg/' + picture3Url + '.jpg'
    if picture4 != '':
        picture4Url = str(uuid.uuid1())
        fileName = r'templates/static/topicImg/' + picture4Url + '.jpg'
        file = open(fileName, 'wb')
        picture4 = base64.b64decode(picture4)
        file.write(picture4)
        file.close()
        picture4 = '/static/topicImg/' + picture4Url + '.jpg'
    if picture5 != '':
        picture5Url = str(uuid.uuid1())
        fileName = r'templates/static/topicImg/' + picture5Url + '.jpg'
        file = open(fileName, 'wb')
        picture5 = base64.b64decode(picture5)
        file.write(picture5)
        file.close()
        picture5 = '/static/topicImg/'+picture5Url+'.jpg'

    result = topicDao.insertTopic(userId, content, picture1, picture2, picture3, picture4, picture5)
    if result == 0:
        data = {'code': 1, 'msg': '发表话题失败'}
    else:
        data = {'code': 0}
    return data


# 删除话题
def removeTopic(session_id, topicId):
    if session_id == '':
        data = {'code': 1, 'msg': 'session_id不能为空'}
        return data
    if topicId == '':
        data = {'code': 1, 'msg': 'topicId不能为空'}
        return data
    userId = redisCon.get(session_id)
    if userId is None:
        data = {'code': 1, 'msg': '请先登录'}
        return data
    topicId = int(topicId)
    result = topicDao.deleteTopic(topicId)
    if result == 1:
        data = {'code': 0, 'msg': '话题删除成功'}
    else:
        data = {'code': 1, 'msg': '话题无法删除'}
    return data

# 获取回复用户的跟帖和跟帖评论
def retrieveUserReplyAndSubReplyByUserId(session_id, x, n):
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
        data = {'code': 1, 'msg': '暂时无法失败'}
        return data
    replyData = replyDao.selectFromXGetNReplyByUserId(userId, x, n)
    subreplyData = subReplyDao.selectFromXGetNSubReplyByUserId(userId, x, n)
    if replyData is None or subreplyData is None:
        data = {'code': 1, 'msg': '暂时无法失败'}
        return data
    data = []
    totalReply = replyDao.selectSumReplyByUserId(userId)
    totalSubReply = subReplyDao.selectSumSubReplyByUserId(userId)
    total = totalReply + totalSubReply
    for reply in replyData:
        replyId = reply.replyId
        topicId = reply.topicId
        time = reply.replyTime.strftime('%Y-%m-%d %H:%M:%S')
        replyContent = reply.content[:20]
        likes = reply.likes
        topicData = topicDao.selectTopicByTopicId(topicId)
        topicContent = topicData.content[:20]
        rep = {'type': 'reply',
               'replyId': replyId,
               'topicId': topicId,
               'time': time,
               'replyContent': replyContent,
               'topicContent': topicContent,
               'likes': likes
               }
        data.append(rep)
    for subreply in subreplyData:
        subreplyId = subreply.subreplyId
        replyId = subreply.replyId
        time = subreply.subreplyTime.strftime('%Y-%m-%d %H:%M:%S')
        subreplyContent = subreply.content[:20]
        likes = subreply.likes
        reply = replyDao.selectReplyByReplyId(replyId)
        replyContent = reply.content[:20]
        floor = reply.floor
        topicId = reply.topicId
        sub = {'type': 'subreply',
               'subreplyId': subreplyId,
               'replyId': replyId,
               'topicId': topicId,
               'time': time,
               'subreplyContent': subreplyContent,
               'likes': likes,
               'replyContent': replyContent,
               'floor': floor}
        data.append(sub)
    data = sorted(data, key=lambda e: e.__getitem__('time'), reverse=True)
    data = {'code': 0, 'data': data, 'total': total}
    return data

# 管理员获取话题
def adminGetFromXGetNTopic(session_id, x, n):
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
        data = {'code': 1, 'msg': '话题获取失败'}
        return data
    result = topicDao.selectFromXGetNTopic(x, n)
    if result is None:
        data = {'code': 1, 'msg': '话题获取失败'}
        return data
    else:
        data = []
        total = topicDao.selectSumTopic()
        for topic in result:
            topicId = topic.topicId
            userId = topic.userId
            lastTime = topic.lastTime.strftime('%Y-%m-%d %H:%M:%S')
            content = topic.content[:40]
            picture1 = topic.picture1
            picture2 = topic.picture2
            picture3 = topic.picture3
            replyNum = topic.replyNum
            comNum = topic.comNum
            user = usersDao.selectUserByUserId(userId)
            if user is None:
                data = {'code': 1, 'msg': '话题获取失败'}
                return data
            username = user['username']
            iconUrl = user['iconUrl']

            top = {'topicId': topicId,
                   'userId': userId,
                   'username': username,
                   'iconUrl': iconUrl,
                   'lastTime': lastTime,
                   'content': content,
                   'picture1': picture1,
                   'picture2': picture2,
                   'picture3': picture3,
                   'replyNum': replyNum,
                   'comNum': comNum}
            data.append(top)
        data = {'code': 0, 'rows': data, 'total': total}
    return data