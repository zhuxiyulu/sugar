from domain.database import DBSession
from domain.topic import Topic
import datetime

# 获取最新话题列表
def selectLastTopicList(topicIdList, n):
    try:
        session = DBSession()
        topic = session.query(Topic).filter(Topic.topicId.notin_(topicIdList)).order_by(Topic.lastTime.desc()).limit(n).all()
        if topic is None:
            result = None
        else:
            result = topic
    except Exception:
        raise
    else:
        session.close()
    return result


# 根据topicId获取话题
def selectTopicByTopicId(topicId):
    try:
        session = DBSession()
        topic = session.query(Topic).filter(Topic.topicId == topicId).first()
        if topic is None:
            result = None
        else:
            result = topic
    except Exception:
        raise
    else:
        session.close()
    return result

# 修改话题的跟帖数
def updateReplyNum(topicId, num):
    try:
        session = DBSession()
        topic = session.query(Topic).filter(Topic.topicId == topicId).first()
        if topic is None:
            return 0
        else:
            topic.replyNum = topic.replyNum + num
            if topic.replyNum < 0:
                topic.replyNum = 0
    except Exception:
        session.rollback()
        raise
    else:
        session.commit()
        session.close()
        return 1

# 修改评论数
def updateComnumber(topicId, num):
    try:
        session = DBSession()
        topic = session.query(Topic).filter(Topic.topicId == topicId).first()
        if topic is None:
            return 0
        else:
            topic.comNum = topic.comNum + num
            if topic.comNum < 0:
                topic.comNum = 0
    except Exception:
        session.rollback()
        raise
    else:
        session.commit()
        session.close()
        return 1

# 添加话题的点赞数
def updateLikes(topicId, likes):
    try:
        session = DBSession()
        topic = session.query(Topic).filter(Topic.topicId == topicId).first()
        if topic is None:
            return 0
        else:
            topic.likes = topic.likes + likes
    except Exception:
        session.rollback()
        raise
    else:
        session.commit()
        session.close()
        return 1

# 获取用户发布的话题列表
def selectFromXGetNTopicByUserId(userId, x, n):
    try:
        session = DBSession()
        offset = x
        num = x + n
        topic = session.query(Topic).filter(Topic.userId == userId).slice(offset, num).all()
        if topic is None:
            result = None
        else:
            result = topic
    except Exception:
        raise
    else:
        session.close()
        return result

# 搜索话题
def selectTopicLikeContent(content, x, n):
    try:
        session = DBSession()
        offset = x
        num = x + n
        topic = session.query(Topic).filter(Topic.content.like('%'+content+'%')).slice(offset, num).all()
        if topic is None:
            result = None
        else:
            result = topic
    except Exception:
        raise
    else:
        session.close()
        return result

# 搜索话题总数
def selectSumTopicLikeContent(content):
    try:
        session = DBSession()
        result = session.query(Topic).filter(Topic.content.like('%'+content+'%')).count()
    except Exception:
        raise
    else:
        session.close()
        return result

# 删除话题
def deleteTopic(topicId):
    effect_raw = 0
    try:
        session = DBSession()
        topic = session.query(Topic).filter(Topic.topicId == topicId).first()
        if topic is None:
            effect_raw = 0
            return effect_raw
        else:
            session.query(Topic).filter_by(topicId=topicId).delete()
            effect_raw = 1
    except:
        session.rollback()
        effect_raw = 0
    else:
        session.commit()
        session.close()
    return effect_raw

# 添加话题
def insertTopic(userId, content, picture1, picture2, picture3, picture4, picture5):
    topicTime = datetime.datetime.now()
    lastTime = datetime.datetime.now()
    edTopic = Topic(content=content,
                    topicTime=topicTime,
                    userId=userId,
                    lastTime=lastTime,
                    picture1=picture1,
                    picture2=picture2,
                    picture3=picture3,
                    picture4=picture4,
                    picture5=picture5,
                    likes=0,
                    replyNum=0,
                    comNum=0)
    effect_row = 0
    try:
        session = DBSession()
        session.add(edTopic)
    except Exception:
        session.rollback()
        raise
    else:
        session.commit()
        effect_row = 1
        session.close()
    return effect_row

# 更新话题最后回复时间
def updateTopicLastTime(topicId):
    try:
        session = DBSession()
        topic = session.query(Topic).filter(Topic.topicId == topicId).first()
        if topic is None:
            return 0
        else:
            topic.lastTime = datetime.datetime.now()
    except Exception:
        session.rollback()
        raise
    else:
        session.commit()
        session.close()
        return 1

# 从X开始获取N个话题
def selectFromXGetNTopic(x, n):
    try:
        session = DBSession()
        offset = x
        num = x + n
        topic = session.query(Topic).slice(offset, num).all()
    except Exception:
        raise
    else:
        session.close()
        return topic

# 获取话题总数
def selectSumTopic():
    result = 0
    try:
        session = DBSession()
        result = session.query(Topic).count()
    except Exception:
        raise
    else:
        session.close()
        return result

# 获取用户的话题总数
def selectSumTopicByUserId(userId):
    result = 0
    try:
        session = DBSession()
        result = session.query(Topic).filter(Topic.userId == userId).count()
    except Exception:
        raise
    else:
        session.close()
        return result
