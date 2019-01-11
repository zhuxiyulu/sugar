from tornado.web import RequestHandler
from tornado.web import gen
from controller import favoriteTopicController
import json

# 收藏话题
class AddFavoriteTopic(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        topicId = self.get_argument('topicId')
        data = favoriteTopicController.createFavoriteTopic(session_id, topicId)
        self.write(json.dumps(data))

# 取消收藏的话题
class RemoveFavoriteTopic(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        topicId = self.get_argument('topicId')
        data = favoriteTopicController.removeFavoriteTopic(session_id, topicId)
        self.write(json.dumps(data))


# 获取用户收藏的话题
class GetFavoriteTopic(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        x = self.get_argument('x')
        n = self.get_argument('n')
        data = favoriteTopicController.retrieveFavoriteTopic(session_id, x, n)
        self.write(json.dumps(data))
