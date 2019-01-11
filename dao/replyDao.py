from domain.database import DBSession
from domain.reply import Reply
import datetime

# 从x位置获取n个跟帖
def selectReplyFromXGetN(topicId, x, n):
    try:
        session = DBSession()
        offset = x
        num = x + n
        reply = session.query(Reply).filter(Reply.topicId == topicId, Reply.isRemove == 0).order_by(Reply.floor).slice(offset, num).all()
        if reply is None:
            result = None
        else:
            result = reply
    except Exception:
        raise
    else:
        session.close()
        return result

# 修改评论数
def updateComNumber(replyId, num):
    try:
        session = DBSession()
        reply = session.query(Reply).filter(Reply.replyId == replyId).first()
        if reply is None:
            return 0
        else:
            reply.comNumber = reply.comNumber + num
            if reply.comNumber < 0:
                reply.comNumber = 0
    except Exception:
        session.rollback()
        raise
    else:
        session.commit()
        session.close()
        return 1

# 通过id获取跟帖
def selectReplyByReplyId(replyId):
    try:
        session = DBSession()
        reply = session.query(Reply).filter(Reply.replyId == replyId).first()
        if reply is None:
            result = None
        else:
            result = reply
    except Exception:
        raise
    else:
        session.close()
    return result

# 修改跟帖的点赞数
def updateLikes(replyId, likes):
    try:
        session = DBSession()
        reply = session.query(Reply).filter(Reply.replyId == replyId).first()
        if reply is None:
            return 0
        else:
            reply.likes = reply.likes + likes
    except Exception:
        session.rollback()
        raise
    else:
        session.commit()
        session.close()
        return 1

# 删除跟帖
def deleteReply(replyId):
    effect_raw = 0
    try:
        session = DBSession()
        reply = session.query(Reply).filter(Reply.replyId == replyId, Reply.isRemove == 0).first()
        if reply is None:
            effect_raw = 0
            return effect_raw
        else:
            reply.isRemove = 1
            effect_raw = 1
    except:
        session.rollback()
        effect_raw = 0
    else:
        session.commit()
        session.close()
    return effect_raw

# 根据userId获取跟帖
def selectFromXGetNReplyByUserId(userId, x, n):
    try:
        session = DBSession()
        offset = x
        num = x + n
        reply = session.query(Reply).filter(Reply.userId == userId, Reply.isRemove == 0).order_by(Reply.replyTime.desc()).slice(offset, num).all()
        if reply is None:
            result = None
        else:
            result = reply
    except Exception:
        raise
    else:
        session.close()
        return result

# 根据topicId 获取最后的楼层
def selectFloorByTopicId(topicId):
    try:
        session = DBSession()
        reply = session.query(Reply).filter(Reply.topicId == topicId).all()
        if reply is None:
            result = None
        else:
            result = reply
    except Exception:
        raise
    else:
        session.close()
        return result

# 添加跟帖
def insertReply(userId, topicId, content, picture1, picture2, picture3, picture4, picture5):
    replyTime = datetime.datetime.now()
    result = selectFloorByTopicId(topicId)
    i = len(result)
    if i == 0:
        floor = 1
    else:
        reply = result[i - 1]
        floor = reply.floor + 1

    edTopic = Reply(content=content,
                    replyTime=replyTime,
                    userId=userId,
                    topicId=topicId,
                    comNumber=0,
                    floor=floor,
                    likes=0,
                    isRemove=0,
                    picture1=picture1,
                    picture2=picture2,
                    picture3=picture3,
                    picture4=picture4,
                    picture5=picture5
                    )
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

# 获取跟帖总数
def selectSumReply():
    result = 0
    try:
        session = DBSession()
        result = session.query(Reply).count()
    except Exception:
        raise
    else:
        session.close()
        return result

# 获取某个话题的跟帖总数
def selectSumReplyByTopicId(topicId):
    result = 0
    try:
        session = DBSession()
        result = session.query(Reply).filter(Reply.topicId == topicId).count()
    except Exception:
        raise
    else:
        session.close()
        return result

# 获取某个用户的跟帖总数
def selectSumReplyByUserId(userId):
    result = 0
    try:
        session = DBSession()
        result = session.query(Reply).filter(Reply.userId == userId).count()
    except Exception:
        raise
    else:
        session.close()
        return result
