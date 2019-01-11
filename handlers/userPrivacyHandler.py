from tornado.web import RequestHandler
from tornado.web import gen
from controller import userPrivacyController
import json

# 更新用户隐私设置
class AlterUserPrivacy(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        isTel = self.get_argument('isTel')
        isGender = self.get_argument('isGender')
        isAge = self.get_argument('isAge')
        isHeight = self.get_argument('isHeight')
        isWeight = self.get_argument('isWeight')
        isArea = self.get_argument('isArea')
        isJob = self.get_argument('isJob')
        isIntegral = self.get_argument('isIntegral')
        data = userPrivacyController.editUserPrivacy(session_id,  isTel, isGender,  isAge, isHeight, isWeight, isArea, isJob, isIntegral)
        self.write(json.dumps(data))

# 查询用户的隐私设置
class GetUserPrivacy(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        data = userPrivacyController.retrieveUserPrivacy(session_id)
        self.write(json.dumps(data))