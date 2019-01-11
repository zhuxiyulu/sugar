from dao import articleDao
from dao import favoriteArticleDao
from dao.sessionDao import redisCon

# 添加文章
def createArticle(title, content):
    if title == '':
        data = {'code': 1, 'msg': '文章标题不能为空'}
        return data
    if content == '':
        data = {'code': 1, 'msg': '文章内容不能为空'}
        return data

    effect_row = articleDao.insertArticle(title, content)
    if effect_row == 1:
        data = {'code': 0}
    else:
        data = {'code': 1, 'msg': '文章添加成功'}

    return data

# 删除一篇文章
def removeArticle(articleId):
    if articleId == '':
        data = {'code': 1, 'msg': 'articleId不能为空'}
        return data
    articleId = int(articleId)
    result = articleDao.deleteArticle(articleId)
    if result == 1:
        data = {'code': 0, 'msg': '文章删除成功'}
    else:
        data = {'code': 1, 'msg': '文章删除失败'}
    return data


# 查看一篇文章
def retrieveArticle(articleId):
    if articleId == '':
        data = {'code': 1, 'msg': 'articleId不能为空'}
        return data

    articleId = int(articleId)
    article = articleDao.selectArticle(articleId)
    if article is None:
        data = {'code': 1, 'msg': '查看文章失败'}
    else:
        title = article.title
        content = article.content
        articleTime = article.articleTime.strftime('%Y-%m-%d %H:%M:%S')
        labelOne = article.labelOne
        labelTwo = article.labelTwo
        labelThree = article.labelThree
        labelFour = article.labelFour
        labelFive = article.labelFive

        data = {'code': 0,
                'title': title,
                'content': content,
                'articleTime': articleTime,
                'labelOne': labelOne,
                'labelTwo': labelTwo,
                'labelThree': labelThree,
                'labelFour': labelFour,
                'labelFive': labelFive}
    return data

# 修改一篇文章
def editArticle(articleId, title, content):
    if articleId == '':
        data = {'code': 1, 'msg': 'articleId不能为空'}
        return data
    if title == '':
        data = {'code': 1, 'msg': '文章标题不能为空'}
        return data
    if content == '':
        data = {'code': 1, 'msg': '文章内容不能为空'}
        return data
    articleId = int(articleId)
    result = articleDao.updateArticle(articleId, title, content)
    if result == 0:
        data = {'code': 1, 'msg': '暂时无法修改'}
    else:
        data = {'code': 0}
    return data

# 根据文章的articleId，返回图片的url
def getImgUrlByArticleId(articleId):
     if articleId == '':
         data = {'code': 1, 'msg': 'articleId不能为空'}
         return data
     result = articleDao.selectImgUrlByArticleId(articleId)
     if result is None:
         data = {'code': 1, 'msg': '无法获取图片url'}
     else:
         lableOne = result['labelOne']
         lableTwo = result['labelTwo']
         imgId = result['imgId']
         imgId = str(imgId)
         pathOne = 'type1'
         pathTwo = 'diet'
         # 路径字典
         pathDict = {
             '1型糖尿病': 'type1/',
             '2型糖尿病': 'type2/',
             '糖尿病前期': 'early/',
             '基础知识': 'knows/',
             '糖尿病新闻': 'news/',
             '预防糖尿病': 'prevent/',
             '常识': 'knows/',
             '监测': 'monitor/',
             '经验': 'experience/',
             '饮食': 'diet/',
             '运动': 'sport/',
             '治疗': 'treat/',
             '': '',
         }

         pathOne = pathDict[lableOne]
         pathTwo = pathDict[lableTwo]
         imgUrl = '/static/articleImg/' + pathOne + pathTwo + imgId + '.jpg'
         data = {'code': 0, 'imgUrl': imgUrl}
     return data

# 获取最新的n个文章
def getTopNewestArticle(topN):
    if topN == '':
        data = {'code': 1, 'msg': 'topN不能为空'}
        return data
    topN = int(topN)
    result = articleDao.selectTopNewestArticle(topN)
    if result is None:
        data = {'code': 1, 'msg': '无法获取最新N篇文章'}
    else:
        data = []
        for article in result:
            articleId = article.articleId
            title = article.title
            content = article.content[:30]
            articleTime = article.articleTime.strftime('%Y-%m-%d %H:%M:%S')
            imgData = getImgUrlByArticleId(articleId)
            imgUrl = imgData['imgUrl']
            art = {'articleId': articleId, 'title': title, 'content': content, 'articleTime': articleTime, 'imgUrl': imgUrl}
            data.append(art)
        data = {'code': 0, 'data': data}
    return data

# 从x位置获取后面n篇文章
def getFromXGetNArticle(session_id, x, n):
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
        data = {'code': 1, 'msg': '文章获取失败'}
        return data
    result = articleDao.selectFromXGetNArticle(x, n)
    if result is None:
        data = {'code': 1, 'msg': '无法获取x之后n篇文章'}
    else:
        data = []
        total = articleDao.selectSumArticle()
        for article in result:
            articleId = article.articleId
            title = article.title
            content = article.content[:30]
            articleTime = article.articleTime.strftime('%Y-%m-%d %H:%M:%S')
            imgData = getImgUrlByArticleId(articleId)
            imgUrl = imgData['imgUrl']
            views = article.views
            art = {'articleId': articleId,
                   'title': title,
                   'content': content,
                   'articleTime': articleTime,
                   'imgUrl': imgUrl,
                   'views': views
                   }
            data.append(art)
        data = {'code': 0, 'data': data, 'total': total}
    return data

# 搜索文章
def getArticleLikeTitle(session_id, labelName, keyword, x, n):
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
    labelList = eval(labelName)
    while len(labelList) < 5:
        labelList.append('')
    labelOne = str(labelList[0])
    labelTwo = str(labelList[1])
    labelThree = str(labelList[2])
    labelFour = str(labelList[3])
    labelFive = str(labelList[4])
    x = int(x)
    n = int(n)
    if n <= 0 or x < 0:
        data = {'code': 1, 'msg': '搜索失败'}
        return data
    result = articleDao.selectArticleLikeTitle(labelOne, labelTwo, labelThree, labelFour, labelFive, keyword, x, n)
    if result is None:
        data = {'code': 1, 'msg': '无法搜索文章'}
    else:
        data = []
        total = articleDao.selectSumArticleLikeTitle(labelOne, labelTwo, labelThree, labelFour, labelFive, keyword)
        for article in result:
            articleId = article.articleId
            title = article.title
            content = article.content[:30]
            articleTime = article.articleTime.strftime('%Y-%m-%d %H:%M:%S')
            imgData = getImgUrlByArticleId(articleId)
            imgUrl = imgData['imgUrl']
            views = article.views
            art = {'articleId': articleId,
                   'title': title,
                   'content': content,
                   'articleTime': articleTime,
                   'imgUrl': imgUrl,
                   'views': views
                   }
            data.append(art)
        data = {'code': 0, 'data': data, 'total': total}
    return data

# 用户查看一篇文章
def userRetrieveArticle(session_id, articleId):
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
    userId = int(userId)
    articleId = int(articleId)
    articleData = articleDao.selectArticle(articleId)
    favoriteData = favoriteArticleDao.seletcFavoriteArticle(userId, articleId)
    if favoriteData == 1:
        favorite = 1
    else:
        favorite = 0
    if articleData is None:
        data = {'code': 1, 'msg': '查看文章失败'}
    else:
        title = articleData.title
        contentUrl = '/getArticle?articleId='+str(articleId)
        comNumber = articleData.comNumber
        data = {'code': 0,
                'title': title,
                'contentUrl': contentUrl,
                'comNumber': comNumber,
                'favorite': favorite
                }
    return data



# 管理员从x位置获取后面n篇文章
def adminGetFromXGetNArticle(session_id, x, n):
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
        data = {'code': 1, 'msg': '文章获取失败'}
        return data
    result = articleDao.selectFromXGetNArticle(x, n)
    if result is None:
        data = {'code': 1, 'msg': '无法获取x之后n篇文章'}
    else:
        data = []
        total = articleDao.selectSumArticle()
        for article in result:
            articleId = article.articleId
            title = article.title
            content = article.content[:30]
            articleTime = article.articleTime.strftime('%Y-%m-%d %H:%M:%S')
            imgData = getImgUrlByArticleId(articleId)
            imgUrl = imgData['imgUrl']
            views = article.views
            art = {'articleId': articleId,
                   'title': title,
                   'content': content,
                   'articleTime': articleTime,
                   'imgUrl': imgUrl,
                   'views': views
                   }
            data.append(art)
        data = {'total': total, 'rows': data, 'code': 0}
    return data
