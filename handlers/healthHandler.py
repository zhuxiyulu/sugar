from tornado.web import RequestHandler
from tornado.web import gen
from controller import healthController
import json

# 保存健康记录
class SaveHealthRecords(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        insulin = self.get_argument('insulin')
        sportTime = self.get_argument('sportTime')
        weight = self.get_argument('weight')
        bloodPressure = self.get_argument('bloodPressure')
        healthTime = self.get_argument('healthTime')
        healthDate = self.get_argument('healthDate')
        data = healthController.editHealth(session_id, insulin, sportTime, weight, bloodPressure, healthTime, healthDate)
        self.write(json.dumps(data))

# 查看健康记录
class GetHealthRecords(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        x = self.get_argument('x')
        n = self.get_argument('n')
        data = healthController.retrieveUserHealth(session_id, x, n)
        self.write(json.dumps(data))

# 精确获取用户某一天健康记录
class GetUserOneDayHealthRecords(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        healthDate = self.get_argument('healthDate')
        data = healthController.retrieveUserOneDayHealth(session_id, healthDate)
        self.write(json.dumps(data))
