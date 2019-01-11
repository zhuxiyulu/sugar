from tornado.web import RequestHandler
from tornado.web import gen
from controller import favoriteArticleController
import json

# 收藏文章
class AddFavoriteArticle(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        articleId = self.get_argument('articleId')
        data = favoriteArticleController.createFavoriteArticle(session_id, articleId)
        self.write(json.dumps(data))

# 取消收藏的文章
class RemoveFavoriteArticle(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        articleId = self.get_argument('articleId')
        data = favoriteArticleController.removeFavoriteArticle(session_id, articleId)
        self.write(json.dumps(data))


# 获取用户收藏的文章
class GetFavoriteArticle(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        x = self.get_argument('x')
        n = self.get_argument('n')
        data = favoriteArticleController.retrieveFavoriteArticle(session_id, x, n)
        self.write(json.dumps(data))
