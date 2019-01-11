from dao import favoriteTopicDao
from dao.sessionDao import redisCon
from dao import topicDao
from dao import usersDao

# 收藏话题
def createFavoriteTopic(session_id, topicId):
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
    effect_row = favoriteTopicDao.seletcFavoriteTopic(userId, topicId)
    if effect_row == 1:
        data = {'code': 1, 'msg': '您已经收藏了这个话题'}
    else:
        effect_row = favoriteTopicDao.insertFavoriteTopic(userId, topicId)
        if effect_row == 1:
            data = {'code': 0}
        else:
            data = {'code': 1, 'msg': '话题无法收藏'}
    return data


# 取消收藏的话题
def removeFavoriteTopic(session_id, topicId):
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
    effect_row = favoriteTopicDao.deleteFavoriteTopic(userId, topicId)
    if effect_row == 1:
        data = {'code': 0}
    else:
        data = {'code': 1, 'msg': '已取消收藏'}
    return data


# 获取用户收藏的话题
def retrieveFavoriteTopic(session_id, x, n):
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
    userId = int(userId)
    x = int(x)
    n = int(n)
    if x < 0 or n <= 0:
        data = {'code': 1, 'msg': '获取收藏的话题失败'}
        return data
    favoriteData = favoriteTopicDao.seletcUserFavoriteTopic(userId, x, n)
    if favoriteData is None:
        data = {'code': 1, 'msg': '获取收藏的话题失败'}
    else:
        data = []
        total = favoriteTopicDao.selectSumFavoriteTopicByUserId(userId)
        for favorite in favoriteData:
            topicId = favorite.topicId
            topic = topicDao.selectTopicByTopicId(topicId)
            user = usersDao.selectUserByUserId(userId)
            if topic is None or user is None:
                data = {'code': 1, 'msg': '获取收藏的话题失败'}
                return data

            content = topic.content[:40]
            picture1 = topic.picture1
            picture2 = topic.picture2
            picture3 = topic.picture3
            iconUrl = user['iconUrl']
            username = user['username']

            data.append({'topicId': topicId,
                         'content': content,
                         'picture1': picture1,
                         'picture2': picture2,
                         'picture3': picture3,
                         'userId': userId,
                         'iconUrl': iconUrl,
                         'username': username
                        })
        data = {'code': 0, 'data': data, 'total': total}
    return data