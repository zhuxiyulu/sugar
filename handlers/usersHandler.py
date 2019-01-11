from tornado.web import RequestHandler
from tornado.web import HTTPError
from tornado.web import gen
from controller import usersController
from controller import codeController
import json

# 获取验证码
class GetCodeHandler(RequestHandler):
    @gen.coroutine
    def post(self):
        tel = self.get_argument('tel')
        data = codeController.getVerifyCode(tel)
        self.write(json.dumps(data))

# 注册
class RegisterHandler(RequestHandler):
    @gen.coroutine
    def get(self):
        self.write_error(HTTPError(400))
    def post(self):
        tel = self.get_argument('tel')
        username = self.get_argument('username')
        verifyCode = self.get_argument('verifyCode')
        password = self.get_argument('password')
        data = usersController.createUser(tel, username, verifyCode, password)
        self.write(json.dumps(data))

# 登录
class LoginHandler(RequestHandler):
    @gen.coroutine
    def get(self):
        self.write_error(HTTPError(400))
    def post(self):
        tel = self.get_argument('tel')
        password = self.get_argument('password')
        data = usersController.userLoginVerify(tel, password)
        self.write(json.dumps(data))

# 登出
class LogoutHandler(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        data = usersController.userLogout(session_id)
        self.write(json.dumps(data))

# 通过session_id获取用户个人信息
class GetUserInfoBySessionId(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        data = usersController.retrieveUserBySessionId(session_id)
        self.write(json.dumps(data))

# 通过session_id，otherUserId获取其他用户信息
class GetOtherUserInfoByUserId(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        otherUserId = self.get_argument('otherUserId')
        data = usersController.retrieveOtherUserInfoByUserId(session_id, otherUserId)
        self.write(json.dumps(data))

# 修改一个用户信息
class AlterUserInfoHandler(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        username = self.get_argument('username')
        gender = self.get_argument('gender')
        age = self.get_argument('age')
        height = self.get_argument('height')
        weight = self.get_argument('weight')
        area = self.get_argument('area')
        job = self.get_argument('job')
        data = usersController.editUser(session_id, username, gender, age, height, weight, area, job)
        self.write(json.dumps(data))

# 更新用户积分
class AlterUserIntegralHandler(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        intrgral = self.get_argument('integral')
        data = usersController.editUserIntegral(session_id, intrgral)
        self.write(json.dumps(data))

# 删除用户
class RemoveUserHandler(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        userId = self.get_argument('userId')
        data = usersController.removeUser(session_id)
        self.write(json.dumps(data))

# 从x位置获取后面n个用户
class GetFromXGetNUser(RequestHandler):
    @gen.coroutine
    def post(self):
        x = self.get_argument('x')
        n = self.get_argument('n')
        data = usersController.getFromXGetNUser(x, n)
        self.write(json.dumps(data))

# 修改密码
class AlterUserPassword(RequestHandler):
    @gen.coroutine
    def post(self):
        tel = self.get_argument('tel')
        verifyCode = self.get_argument('verifyCode')
        password= self.get_argument('password')
        data = usersController.editUserPassword(tel, verifyCode, password)
        self.write(json.dumps(data))

# 用户签到
class AlterUserCheckTime(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        data = usersController.editUserCheckTime(session_id)
        self.write(json.dumps(data))

# 管理员从x位置获取后面n个用户
class AdminGetFromXGetNUser(RequestHandler):
    @gen.coroutine
    def post(self):
        session_id = self.get_argument('session_id')
        x = self.get_argument('x')
        n = self.get_argument('n')
        data = usersController.adminGetFromXGetNUser(session_id, x, n)
        self.write(json.dumps(data))