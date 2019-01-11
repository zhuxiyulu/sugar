#!/usr/bin/env python
# coding=utf-8

# 后台
# from handlers.indexHandler import IndexHandler
# from handlers.indexHandler import UsersAdminHandler
# from handlers.indexHandler import AdminLoginHandler
# from handlers.indexHandler import AdminArticleHandler
# from handlers.indexHandler import AdminEditArticleHandler
# from handlers.usersHandler import AdminGetFromXGetNUser
# from handlers.articleHandler import AdminGetFromXGetNArticle
# from handlers.indexHandler import AdminTopicHandler
# from handlers.topicHandler import AdminGetFromXGetNTopic

# 用户
from handlers.usersHandler import GetCodeHandler
from handlers.usersHandler import RegisterHandler
from handlers.usersHandler import LoginHandler
from handlers.usersHandler import LogoutHandler
from handlers.usersHandler import GetUserInfoBySessionId
from handlers.usersHandler import GetOtherUserInfoByUserId
from handlers.usersHandler import AlterUserInfoHandler
from handlers.usersHandler import AlterUserIntegralHandler
from handlers.usersHandler import RemoveUserHandler
from handlers.usersHandler import AlterUserPassword
from handlers.usersHandler import AlterUserCheckTime
from handlers.usersHandler import GetFromXGetNUser


# 隐私设置
from handlers.userPrivacyHandler import AlterUserPrivacy
from handlers.userPrivacyHandler import GetUserPrivacy
# 关注
from handlers.followHandler import AddFollow
from handlers.followHandler import RemoveFollow
from handlers.followHandler import GetFollowList
from handlers.followHandler import GetFollowMeList
# 文章
from handlers.articleHandler import AddArticleHandler
from handlers.articleHandler import RemoveArticleHandler
from handlers.articleHandler import GetArticleHandler
from handlers.articleHandler import AlterArticleHandler
from handlers.articleHandler import GetImgUrlByArticleId
from handlers.articleHandler import GetTopNewestArticle
from handlers.articleHandler import GetFromXGetNArticle
from handlers.articleHandler import SearchArticle
from handlers.articleHandler import UserGetArticle


# 文章收藏
from handlers.favoriteArticleHandler import AddFavoriteArticle
from handlers.favoriteArticleHandler import RemoveFavoriteArticle
from handlers.favoriteArticleHandler import GetFavoriteArticle
# 评论
from handlers.commentHandler import AddCommentHandler
from handlers.commentHandler import GetFromXGetNCommentByArticleId
from handlers.commentHandler import AlterCommentLikes
from handlers.commentHandler import GetCommentByUserId
# 话题
from handlers.topicHandler import GetLastTopicList
from handlers.topicHandler import AlterTopicLikes
from handlers.topicHandler import GetTopicByUserId
from handlers.topicHandler import GetTopicByTopicId
from handlers.topicHandler import SearchTopic
from handlers.topicHandler import RemoveTopic
from handlers.topicHandler import GetUserReplyAndSubReplyByUserId
from handlers.topicHandler import AddTopic

# 话题收藏
from handlers.favoriteTopicHandler import AddFavoriteTopic
from handlers.favoriteTopicHandler import RemoveFavoriteTopic
from handlers.favoriteTopicHandler import GetFavoriteTopic

# 跟帖
from handlers.replyHandler import GetReplyFromXGetN
from handlers.replyHandler import AlterReplyLikes
from handlers.replyHandler import RemoveReply
from handlers.replyHandler import AddReply

# 跟帖评论
from handlers.subreplyHandler import GetSubReplyFromXGetN
from handlers.subreplyHandler import AddSubReply
from handlers.subreplyHandler import AlterSubReplyLikes
from handlers.subreplyHandler import RemoveSubReply

# 糖导
from handlers.sugarGuideHandler import AddSugarGuideResult
from handlers.sugarGuideHandler import GetHealthWeekly

# 血糖
from handlers.bloodHandler import SaveBloodSugar
from handlers.bloodHandler import GetBloodSugar
from handlers.bloodHandler import GetUserOneDayBlood

# 健康记录
from handlers.healthHandler import SaveHealthRecords
from handlers.healthHandler import GetHealthRecords
from handlers.healthHandler import GetUserOneDayHealthRecords

# 家属链接
from handlers.familyHandler import GetUserFamilyList
from handlers.familyHandler import AlterUserFamily

url = [

    # (r'/', AdminLoginHandler),  # 主页
    # (r'/index.html', IndexHandler),  # 主页
    # (r'/users.html', UsersAdminHandler),  # 用户管理
    # (r'/adminGetFromXGetNUser', AdminGetFromXGetNUser),  # 管理员获取用户列表
    # (r'/login.html', AdminLoginHandler),  # 管理员登录
    # (r'/article.html', AdminArticleHandler),  # 文章管理
    # (r'/adminGetFromXGetNArticle', AdminGetFromXGetNArticle),  # 管理员获取文章列表
    # (r'/notepad.html', AdminEditArticleHandler),  # 管理员新增文章
    # (r'/topic.html', AdminTopicHandler),  # 话题管理
    # (r'/adminGetFromXGetNTopic', AdminGetFromXGetNTopic),  # # 管理员获取话题列表

    (r'/getCode', GetCodeHandler),  # 获取验证码
    (r'/register', RegisterHandler),  # 注册
    (r'/login', LoginHandler),  # 登录
    (r'/logout', LogoutHandler),  # 登出
    (r'/getUserInfoBySessionId', GetUserInfoBySessionId),  # 通过session_id查找一个用户信息
    (r'/getOtherUserInfo', GetOtherUserInfoByUserId),  # 通过session_id，otherUserId获取其他用户信息
    (r'/alterUserInfo', AlterUserInfoHandler),  # 修改用户信息
    (r'/alterUserIntegral', AlterUserIntegralHandler),  # 更新用户积分
    (r'/removeUser', RemoveUserHandler),  # 删除用户
    (r'/getFromXGetNUser', GetFromXGetNUser),  # 从x开始获取n个用户
    (r'/alterPassword', AlterUserPassword),  # 修改用户密码
    (r'/alterUserCheckTime', AlterUserCheckTime),  # 用户签到


    (r'/alterUserPrivacy', AlterUserPrivacy),  # 更新用户隐私设置
    (r'/getUserPrivacy', GetUserPrivacy),   # 查询用户权限设置

    (r'/addFollow', AddFollow),  # 关注
    (r'/removeFollow', RemoveFollow),  # 取消关注
    (r'/getFollowList', GetFollowList),  # 用户查看自己关注的列表
    (r'/getFollowMeList', GetFollowMeList),   # 查看关注我的人

    (r'/addArticle', AddArticleHandler),  # 添加一篇文章
    (r'/removeArticle', RemoveArticleHandler),  # 删除一篇文章
    (r'/getArticle', GetArticleHandler),  # 通过articleId获取一篇文章 （详细）
    (r'/userGetArticle', UserGetArticle),  # 某个用户通过articleId获取一篇文章 （详细）
    (r'/alterArticle', AlterArticleHandler),  # 修改文章
    (r'/getImgUrl', GetImgUrlByArticleId),  # 根据文章的articleId，返回图片的url
    (r'/getTopNewestArticle', GetTopNewestArticle),  # 获取最新的n个文章
    (r'/getFromXGetNArticle', GetFromXGetNArticle),  # 从x位置获取后面n篇文章
    (r'/searchArticle', SearchArticle),  # 搜索文章
    (r'/addFavorite', AddFavoriteArticle),  # 收藏文章
    (r'/removeFavorite', RemoveFavoriteArticle),  # 取消收藏的文章
    (r'/getFavoriteArticle', GetFavoriteArticle),   # 用户获取自己收藏的文章

    (r'/addComment', AddCommentHandler),  # 添加评论
    (r'/GetFromXGetNComment', GetFromXGetNCommentByArticleId),  # 从x位置获取文章articleId后面n篇评论
    (r'/alterCommentLikes', AlterCommentLikes),  # 添加评论的点赞数
    (r'/getCommentByUserId', GetCommentByUserId),  # 用户获取评论

    (r'/getLastTopic', GetLastTopicList),  # 获取最新话题列表
    (r'/getTopicByUserId', GetTopicByUserId),  # 获取用户发布的话题
    (r'/getTopicByTopicId', GetTopicByTopicId),  # 根据话题ID获取话题
    (r'/alterTopicLikes', AlterTopicLikes),  # 添加话题的点赞数
    (r'/searchTopic', SearchTopic),  # 搜索话题
    (r'/removeTopic', RemoveTopic),  # 删除话题
    (r'/addTopic', AddTopic),  # 添加话题

    (r'/addFavoriteTopic', AddFavoriteTopic),  # 收藏话题
    (r'/removeFavoriteTopic', RemoveFavoriteTopic),  # 取消收藏的话题
    (r'/getFavoriteTopic', GetFavoriteTopic),  # 获取用户收藏的话题

    (r'/getUserReplyAndSubReply', GetUserReplyAndSubReplyByUserId),  # 获取回复用户的跟帖和跟帖评论
    (r'/getReplyFromXGetN', GetReplyFromXGetN),  # 从x位置获取n个跟帖
    (r'/alterReplyLikes', AlterReplyLikes),  # 添加跟帖的点赞数
    (r'/removeReply', RemoveReply),  # 删除跟帖
    (r'/addReply', AddReply),  # 添加跟帖

    (r'/getSubReplyFromXGetN', GetSubReplyFromXGetN),  # 从x位置获取n个跟帖评论
    (r'/addSubReply', AddSubReply),  # 发表跟帖评论
    (r'/alterSubReplyLikes', AlterSubReplyLikes),   # 添加跟帖评论的点赞数
    (r'/removeSubReply', RemoveSubReply),  # 删除跟帖评论

    (r'/addSugarGuideResult', AddSugarGuideResult),  # 保存糖导数据
    (r'/getHealthWeekly', GetHealthWeekly),  # 获取健康周报

    (r'/saveBloodSugar', SaveBloodSugar),  # 保存血糖记录
    (r'/getBloodSugar', GetBloodSugar),  # 获取血糖记录
    (r'/getUserOneDayBlood', GetUserOneDayBlood),  # 精确获取用户某一天血糖记录

    (r'/saveHealthRecords', SaveHealthRecords),  # 保存健康记录
    (r'/getHealthRecords', GetHealthRecords),  # 查看健康记录
    (r'/getUserOneDayHealthRecords', GetUserOneDayHealthRecords),  # 精确获取用户某一天健康记录

    (r'/getUserFamilyList', GetUserFamilyList),  # 获取家属连接列表
    (r'/alterUserFamily', AlterUserFamily),  # 新建家属链接

]