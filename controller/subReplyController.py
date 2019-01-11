from dao import subReplyDao
from dao.sessionDao import redisCon
from dao import usersDao
from dao import replyDao
from dao import topicDao

# 从x位置获取n个跟帖的评论
def retrieveSubReplyFromXGetN(session_id, replyId, x, n):
    if session_id == '':
        data = {'code': 1, 'msg': 'session_id不能为空'}
        return data
    if replyId == '':
        data = {'code': 1, 'msg': '跟帖ID不能为空'}
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
    replyId = int(replyId)
    x = int(x)
    n = int(n)
    if x < 0 or n <= 0:
        data = {'code': 1, 'msg': '跟帖评论获取失败'}
        return data
    result = subReplyDao.selectSubReplyFromXGetN(replyId, x, n)
    if result is None:
        data = {'code': 1, 'msg': '跟帖评论获取失败'}
        return data
    else:
        data = []
        total = subReplyDao.selectSumSubReplyByReplyId(replyId)
        for subreply in result:
            subreplyId = subreply.subreplyId
            userId = subreply.userId
            subreplyTime = subreply.subreplyTime.strftime('%Y-%m-%d %H:%M:%S')
            content = subreply.content
            likes = subreply.likes

            user = usersDao.selectUserByUserId(userId)
            if user is None:
                data = {'code': 1, 'msg': '跟帖评论获取失败'}
                return data
            username = user['username']
            iconUrl = user['iconUrl']

            subrep = {'subreplyId': subreplyId,
                      'userId': userId,
                      'iconUrl': iconUrl,
                      'username': username,
                      'content': content,
                      'subreplyTime': subreplyTime,
                      'likes': likes
                      }
            data.append(subrep)
        data = {'code': 0, 'data': data}
    return data

# 发表跟帖评论
def createSubReply(session_id, replyId, content):
    if session_id == '':
        data = {'code': 1, 'msg': 'session_id不能为空'}
        return data
    if replyId == '':
        data = {'code': 1, 'msg': '跟帖ID不能为空'}
        return data
    if content == '':
        data = {'code': 1, 'msg': 'content不能为空'}
        return data
    userId = redisCon.get(session_id)
    if userId is None:
        data = {'code': 1, 'msg': '请先登录'}
        return data
    replyId = int(replyId)
    userId = int(userId)
    effect_row = subReplyDao.insertSubReply(userId, replyId, content)
    if effect_row == 1:
        data = {'code': 0}

        # 更新话题评论数量、最后回复时间
        reply = replyDao.selectReplyByReplyId(replyId)
        if reply is not None:
            topicId = reply.topicId
            topicDao.updateComnumber(topicId, 1)
            topicDao.updateTopicLastTime(topicId)

        # 更新跟帖评论数
        replyDao.updateComNumber(replyId, 1)

    else:
        data = {'code': 1, 'msg': '评论失败'}
    return data

# 添加评论的点赞数
def editLikes(session_id, subreplyId, isLike):
    if session_id == '':
        data = {'code': 1, 'msg': 'session_id不能为空'}
        return data
    if subreplyId == '':
        data = {'code': 1, 'msg': '评论ID不能为空'}
        return data
    if isLike == '':
        data = {'code': 1, 'msg': '点赞数不能为空'}
        return data
    userId = redisCon.get(session_id)
    subreplyId = int(subreplyId)
    isLike = int(isLike)
    if isLike != 1 and isLike != -1:
        data = {'code': 1, 'msg': '点赞失败'}
        return data
    if userId is None:
        data = {'code': 1, 'msg': '请先登录'}
        return data
    effect_row = subReplyDao.updateLikes(subreplyId, isLike)
    if effect_row == 1:
        data = {'code': 0}
    else:
        data = {'code': 1, 'msg': '点赞失败'}
    return data

# 删除跟帖的评论
def removeSubReply(session_id, subreplyId):
    if session_id == '':
        data = {'code': 1, 'msg': 'session_id不能为空'}
        return data
    if subreplyId == '':
        data = {'code': 1, 'msg': '跟帖评论ID不能为空'}
        return data
    userId = redisCon.get(session_id)
    if userId is None:
        data = {'code': 1, 'msg': '请先登录'}
        return data
    subreplyId = int(subreplyId)
    subreply = subReplyDao.selectSubReplyBySubReplyId(subreplyId)
    replyId = subreply.replyId
    reply = replyDao.selectReplyByReplyId(replyId)
    topicId = reply.topicId
    result = subReplyDao.deleteSubReply(subreplyId)
    if result == 1:
        # 更新话题中记录的跟帖评论的数量
        topicDao.updateComnumber(topicId, -1)

        # 更新跟帖中记录的跟帖评论的数量
        replyDao.updateComNumber(replyId, -1)

        data = {'code': 0, 'msg': '跟帖评论删除成功'}
    else:
        data = {'code': 1, 'msg': '跟帖评论无法删除'}
    return data
