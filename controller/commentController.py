from dao import commentDao
from dao import usersDao
from dao import articleDao
from dao.sessionDao import redisCon

# 添加评论
def createComment(content, session_id, articleId):
    if content == '':
        data = {'code': 1, 'msg': '评论内容不能为空'}
        return data
    if session_id == '':
        data = {'code': 1, 'msg': 'session_id不能为空'}
        return data
    if articleId == '':
        data = {'code': 1, 'msg': 'articleId不能为空'}
        return data
    userId = redisCon.get(session_id)
    if userId is None:
        data = {'code': 1, 'msg': '请先登录'}
        return data
    effect_row = commentDao.insertComment(content, int(userId), int(articleId))
    if effect_row == 1:
        data = {'code': 0}
        articleDao.updateArticleComNumber(articleId)
    else:
        data = {'code': 1, 'msg': '评论失败'}
    return data

# 从x位置获取文章articleId后面n篇评论
def getFromXGetNCommentByArticleId(session_id, articleId, x, n):
    if session_id == '':
        data = {'code': 1, 'msg': 'session_id不能为空'}
        return data
    if articleId == '':
        data = {'code': 1, 'msg': 'articleId不能为空'}
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
    articleId = int(articleId)
    x = int(x)
    n = int(n)
    if x < 0 or n <= 0:
        data = {'code': 1, 'msg': '评论获取失败'}
        return data
    result = commentDao.selectFromXGetNCommentByArticleId(articleId, x, n)
    if result is None:
        data = {'code': 1, 'msg': '无法获取x之后n个评论'}
    else:
        data = []
        total = commentDao.selectSumCommentByArticleId(articleId)
        for comment in result:
            commentId = comment.commentId
            content = comment.content
            commentTime = comment.commentTime.strftime('%Y-%m-%d %H:%M:%S')
            userId = comment.userId
            likes = comment.likes
            userData = usersDao.selectUserByUserId(userId)
            username = userData['username']
            iconUrl = userData['iconUrl']

            art = {'commentId': commentId,
                   'content': content,
                   'commentTime': commentTime,
                   'userId': userId,
                   'likes': likes,
                   'username': username,
                   'iconUrl': iconUrl
                   }
            data.append(art)
        data = {'code': 0, 'data': data, 'total': total}
    return data

# 添加评论的点赞数
def editLikes(session_id, commentId, isLike):
    if session_id == '':
        data = {'code': 1, 'msg': 'session_id不能为空'}
        return data
    if commentId == '':
        data = {'code': 1, 'msg': '评论ID不能为空'}
        return data
    if isLike == '':
        data = {'code': 1, 'msg': '点赞数不能为空'}
        return data
    userId = redisCon.get(session_id)
    commentId = int(commentId)
    isLike = int(isLike)
    if isLike != 1 and isLike != -1:
        data = {'code': 1, 'msg': '点赞失败'}
        return data
    if userId is None:
        data = {'code': 1, 'msg': '请先登录'}
        return data
    effect_row = commentDao.updateLikes(commentId, isLike)
    if effect_row == 1:
        data = {'code': 0}
    else:
        data = {'code': 1, 'msg': '点赞失败'}
    return data

# 用户获取评论
def retrieveCommentByUserId(session_id, x, n):
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
        data = {'code': 1, 'msg': '获取收藏的文章失败'}
        return data
    commentData = commentDao.selectCommentByUser(userId, x, n)
    if commentData is None:
        data = {'code': 1, 'msg': '无法获取评论'}
    else:
        data = []
        total = commentDao.selectSumCommentByUserId(userId)
        for comment in commentData:
            commentId = comment.commentId
            content = comment.content[:20]
            likes = comment.likes
            commentTime = comment.commentTime.strftime('%Y-%m-%d %H:%M:%S')
            articleId = comment.articleId
            article = articleDao.selectArticle(articleId)
            if article is None:
                data = {'code': 1, 'msg': '无法获取评论'}
            else:
                title = article.title
                com = {'commentId': commentId,
                       'content': content,
                       'title': title,
                       'articleId': articleId,
                       'likes': likes,
                       'commentTime': commentTime
                       }
                data.append(com)
        data = {'code': 0, 'data': data, 'total': total}
    return data