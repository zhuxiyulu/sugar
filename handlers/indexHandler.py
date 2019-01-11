from tornado.web import RequestHandler
from tornado.web import gen

# 主页
class IndexHandler(RequestHandler):
    @gen.coroutine
    def get(self):
        self.render("index.html")

# 用户管理
class UsersAdminHandler(RequestHandler):
    @gen.coroutine
    def get(self):
        self.render('users.html')

# 登录
class AdminLoginHandler(RequestHandler):
    @gen.coroutine
    def get(self):
        self.render('login.html')

# 文章
class AdminArticleHandler(RequestHandler):
    @gen.coroutine
    def get(self):
        self.render('article.html')
        
# 添加文章
class AdminEditArticleHandler(RequestHandler):
    @gen.coroutine
    def get(self):
        self.render('notepad.html')

# 话题管理
class AdminTopicHandler(RequestHandler):
    @gen.coroutine
    def get(self):
        self.render('topic.html')