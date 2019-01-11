from tornado.web import RequestHandler
from tornado.web import gen
from controller import topicController
import json

# 获取最新话题列表
class GetLastTopicList(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        topicIdList = self.get_argument('topicIdList')
        n = self.get_argument('n')
        data = topicController.retrieveLastTopicList(session_id, topicIdList, n)
        self.write(json.dumps(data))


# 话题评论点赞
class AlterTopicLikes(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        topicId = self.get_argument('topicId')
        isLike = self.get_argument('isLike')
        data = topicController.editLikes(session_id, topicId, isLike)
        self.write(json.dumps(data))

# 获取用户发布的话题
class GetTopicByUserId(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        x = self.get_argument('x')
        n = self.get_argument('n')
        data = topicController.retrieveTopicByUserId(session_id, x, n)
        self.write(json.dumps(data))

# 根据话题ID获取话题
class GetTopicByTopicId(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        topicId = self.get_argument('topicId')
        data = topicController.retrieveTopicByTopicId(session_id, topicId)
        self.write(json.dumps(data))

# 搜索话题
class SearchTopic(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        keyword = self.get_argument('keyword')
        x = self.get_argument('x')
        n = self.get_argument('n')
        data = topicController.retrieveTopicLikeTopic(session_id, keyword, x, n)
        self.write(json.dumps(data))

# 删除话题
class RemoveTopic(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        topicId = self.get_argument('topicId')
        data = topicController.removeTopic(session_id, topicId)
        self.write(json.dumps(data))

# 获取回复用户的跟帖和跟帖评论
class GetUserReplyAndSubReplyByUserId(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        x = self.get_argument('x')
        n = self.get_argument('n')
        data = topicController.retrieveUserReplyAndSubReplyByUserId(session_id, x, n)
        self.write(json.dumps(data))

# 发表话题
class AddTopic(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        content = self.get_argument('content')
        pictureList = self.get_argument('pictureList')
        data = topicController.createTopic(session_id, content, pictureList)
        self.write(json.dumps(data))

# 管理员从x位置获取后面n个话题
class AdminGetFromXGetNTopic(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        x = self.get_argument('x')
        n = self.get_argument('n')
        data = topicController.adminGetFromXGetNTopic(session_id, x, n)
        self.write(json.dumps(data))