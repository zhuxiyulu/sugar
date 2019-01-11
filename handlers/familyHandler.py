from tornado.web import RequestHandler
from tornado.web import gen
from controller import familyController
import json

# 获取家属连接列表
class GetUserFamilyList(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        data = familyController.retrieveFamilyList(session_id)
        self.write(json.dumps(data))

# 新建家属链接
class AlterUserFamily(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        tel = self.get_argument('tel')
        nickname = self.get_argument('nickname')
        verifyCode = self.get_argument('verifyCode')
        data = familyController.editFamily(session_id, tel, nickname, verifyCode)
        self.write(json.dumps(data))
