from tornado.web import RequestHandler
from tornado.web import gen
from controller import replyController
import json

# 从x位置获取n个跟帖
class GetReplyFromXGetN(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        topicId = self.get_argument('topicId')
        x = self.get_argument('x')
        n = self.get_argument('n')
        data = replyController.retrieveReplyFromXGetN(session_id, topicId, x, n)
        self.write(json.dumps(data))

# 跟帖评论点赞
class AlterReplyLikes(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        replyId = self.get_argument('replyId')
        isLike = self.get_argument('isLike')
        data = replyController.editLikes(session_id, replyId, isLike)
        self.write(json.dumps(data))

# 删除跟帖
class RemoveReply(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        replyId = self.get_argument('replyId')
        data = replyController.removeReply(session_id, replyId)
        self.write(json.dumps(data))

# 添加跟帖
class AddReply(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        topicId = self.get_argument('topicId')
        content = self.get_argument('content')
        pictureList = self.get_argument('pictureList')
        data = replyController.createReply(session_id, topicId, content, pictureList)
        self.write(json.dumps(data))