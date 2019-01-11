from tornado.web import RequestHandler
from tornado.web import gen
from controller import subReplyController
import json

# 从x位置获取n个跟帖评论
class GetSubReplyFromXGetN(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        replyId = self.get_argument('replyId')
        x = self.get_argument('x')
        n = self.get_argument('n')
        data = subReplyController.retrieveSubReplyFromXGetN(session_id, replyId, x, n)
        self.write(json.dumps(data))

# 发表跟帖评论
class AddSubReply(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        replyId = self.get_argument('replyId')
        content = self.get_argument('content')
        data = subReplyController.createSubReply(session_id, replyId, content)
        self.write(json.dumps(data))

# 跟帖评论评论点赞
class AlterSubReplyLikes(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        subreplyId = self.get_argument('subreplyId')
        isLike = self.get_argument('isLike')
        data = subReplyController.editLikes(session_id, subreplyId, isLike)
        self.write(json.dumps(data))

# 删除跟帖评论
class RemoveSubReply(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        subreplyId = self.get_argument('subreplyId')
        data = subReplyController.removeSubReply(session_id, subreplyId)
        self.write(json.dumps(data))
