from tornado.web import RequestHandler
from tornado.web import gen
from controller import bloodController
import json

# 保存血糖记录
class SaveBloodSugar(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        period = self.get_argument('period')
        bLevel = self.get_argument('bLevel')
        bTime = self.get_argument('bTime')
        bloodDate = self.get_argument('bloodDate')
        data = bloodController.editBlood(session_id, period, bLevel, bTime, bloodDate)
        self.write(json.dumps(data))

# 查看血糖记录
class GetBloodSugar(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        x = self.get_argument('x')
        n = self.get_argument('n')
        data = bloodController.retrieveUserBlood(session_id, x, n)
        self.write(json.dumps(data))

# 精确获取用户某一天血糖记录
class GetUserOneDayBlood(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        bloodDate = self.get_argument('bloodDate')
        data = bloodController.retrieveUserOneDayBlood(session_id, bloodDate)
        self.write(json.dumps(data))