from dao import favoriteArticleDao
from dao.sessionDao import redisCon
from dao import articleDao

# 收藏文章
def createFavoriteArticle(session_id, articleId):
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
    effect_row = favoriteArticleDao.seletcFavoriteArticle(userId, articleId)
    if effect_row == 1:
        data = {'code': 1, 'msg': '您已收藏了这篇文章'}
    else:
        effect_row = favoriteArticleDao.insertFavoriteArticle(userId, articleId)
        if effect_row == 1:
            data = {'code': 0}
        else:
            data = {'code': 1, 'msg': '文章无法收藏'}
    return data


# 取消收藏的文章
def removeFavoriteArticle(session_id, articleId):
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
    effect_row = favoriteArticleDao.deleteFavoriteArticle(userId, articleId)
    if effect_row == 1:
        data = {'code': 0}
    else:
        data = {'code': 1, 'msg': '已取消收藏'}
    return data


# 获取用户收藏的文章
def retrieveFavoriteArticle(session_id, x, n):
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
    favoriteData = favoriteArticleDao.seletcUserFavoriteArticle(userId, x, n)
    if favoriteData is None:
        data = {'code': 1, 'msg': '获取收藏的文章失败'}
    else:
        data = []
        total = favoriteArticleDao.selectSumFavoriteArticleByUserId(userId)
        for favorite in favoriteData:
            articleId = favorite.articleId
            article = articleDao.selectArticle(articleId)
            if article is None:
                data = {'code': 1, 'msg': '获取收藏的文章失败'}
            else:
                title = article.title
                content = article.content[:40]
                data.append({'articleId': articleId, 'title': title, 'content': content})
        data = {'code': 0, 'data': data, 'total': total}
    return data