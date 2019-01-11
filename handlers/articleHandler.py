from tornado.web import RequestHandler
from tornado.web import gen
from controller import articleController
import json

# 添加文章
class AddArticleHandler(RequestHandler):
    @gen.coroutine
    def post(self):
        title = self.get_argument('title')
        content = self.get_argument('content')
        data = articleController.createArticle(title, content)
        self.write(json.dumps(data))

# 删除文章
class RemoveArticleHandler(RequestHandler):
    @gen.coroutine
    def post(self):
        articleId = self.get_argument('articleId')
        data = articleController.removeArticle(articleId)
        self.write(json.dumps(data))

# 后台查看文章
class GetArticleHandler(RequestHandler):
    @gen.coroutine
    def get(self):
        articleId = self.get_argument('articleId')
        data = articleController.retrieveArticle(articleId)
        self.render('showArticle.html', title=data['title'], newsTime=data['articleTime'], content=data['content'])
    # @gen.coroutine
    # def post(self):
    #     articleId = self.get_argument('articleId')
    #     data = articleController.retrieveArticle(articleId)
    #     self.write(json.dumps(data))

# 修改文章
class AlterArticleHandler(RequestHandler):
    @gen.coroutine
    def post(self):
        articleId = self.get_argument('articleId')
        title = self.get_argument('title')
        content = self.get_argument('content')
        data = articleController.editArticle(articleId, title, content)
        self.write(json.dumps(data))

# 根据文章的articleId，获取文章图片Url
class GetImgUrlByArticleId(RequestHandler):
    @gen.coroutine
    def post(self):
        articleId = self.get_argument('articleId')
        data = articleController.getImgUrlByArticleId(articleId)
        self.write(json.dumps(data))

# 获取最新的n个文章
class GetTopNewestArticle(RequestHandler):
    @gen.coroutine
    def post(self):
        topN = self.get_argument('topN')
        data = articleController.getTopNewestArticle(topN)
        self.write(json.dumps(data))

# 从x位置获取后面n篇文章
class GetFromXGetNArticle(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        x = self.get_argument('x')
        n = self.get_argument('n')
        data = articleController.getFromXGetNArticle(session_id, x, n)
        self.write(json.dumps(data))

# 搜索文章
class SearchArticle(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        labelName = self.get_argument('labelName')
        keyword = self.get_argument('keyword')
        x = self.get_argument('x')
        n = self.get_argument('n')
        data = articleController.getArticleLikeTitle(session_id, labelName, keyword, x, n)
        self.write(json.dumps(data))

# 用户查看一篇文章
class UserGetArticle(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        articleId = self.get_argument('articleId')
        data = articleController.userRetrieveArticle(session_id, articleId)
        self.write(json.dumps(data))


# 管理员从x位置获取后面n篇文章
class AdminGetFromXGetNArticle(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        x = self.get_argument('x')
        n = self.get_argument('n')
        data = articleController.adminGetFromXGetNArticle(session_id, x, n)
        self.write(json.dumps(data))