from tornado.web import RequestHandler
from tornado.web import gen
from controller import commentController
import json

# 添加评论
class AddCommentHandler(RequestHandler):
    @gen.coroutine
    def post(self):
        content = self.get_argument('content')
        session_id = self.get_argument('session_id')
        articleId = self.get_argument('articleId')
        data = commentController.createComment(content, session_id, articleId)
        self.write(json.dumps(data))


# 从x位置获取文章articleId后面n篇评论
class GetFromXGetNCommentByArticleId(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        articleId = self.get_argument('articleId')
        x = self.get_argument('x')
        n = self.get_argument('n')
        data = commentController.getFromXGetNCommentByArticleId(session_id, articleId, x, n)
        self.write(json.dumps(data))

# 添加评论的点赞数
class AlterCommentLikes(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        commentId = self.get_argument('commentId')
        isLike = self.get_argument('isLike')
        data = commentController.editLikes(session_id, commentId, isLike)
        self.write(json.dumps(data))

# 用户获取评论
class GetCommentByUserId(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        x = self.get_argument('x')
        n = self.get_argument('n')
        data = commentController.retrieveCommentByUserId(session_id, x, n)
        self.write(json.dumps(data))