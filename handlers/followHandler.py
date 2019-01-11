from tornado.web import RequestHandler
from tornado.web import gen
from controller import followController
import json

# 关注
class AddFollow(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        followId = self.get_argument('followId')
        data = followController.createFollow(session_id, followId)
        self.write(json.dumps(data))

# 取消关注
class RemoveFollow(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        followId = self.get_argument('followId')
        data = followController.removeFollow(session_id, followId)
        self.write(json.dumps(data))

# 用户查看自己关注的列表
class GetFollowList(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        x = self.get_argument('x')
        n = self.get_argument('n')
        data = followController.retrieveFollowList(session_id, x, n)
        self.write(json.dumps(data))

# 查看关注我的人
class GetFollowMeList(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        x = self.get_argument('x')
        n = self.get_argument('n')
        data = followController.retrieveFollowMeList(session_id, x, n)
        self.write(json.dumps(data))

