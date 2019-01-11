from domain.database import DBSession
from domain.subreply import SubReply
import datetime

# 从x位置获取n个跟帖的评论
def selectSubReplyFromXGetN(replyId, x, n):
    try:
        session = DBSession()
        offset = x
        num = x + n
        subreply = session.query(SubReply).filter(SubReply.replyId == replyId).slice(offset, num).all()
        if subreply is None:
            result = None
        else:
            result = subreply
    except Exception:
        raise
    else:
        session.close()
        return result

# 发表跟帖评论
def insertSubReply(userId, replyId, content):
    effect_raw = 0
    try:
        session = DBSession()
        subreplyTime = datetime.datetime.now()
        adSubReply = SubReply(content=content, subreplyTime=subreplyTime, replyId=replyId, userId=userId, likes=0)
        session.add(adSubReply)
    except Exception:
        session.rollback()
        raise
    else:
        session.commit()
        session.close()
        effect_raw = 1
    return effect_raw

# 修改跟帖评论的点赞数
def updateLikes(subreplyId, likes):
    try:
        session = DBSession()
        subreply = session.query(SubReply).filter(SubReply.subreplyId == subreplyId).first()
        if subreply is None:
            return 0
        else:
            subreply.likes = subreply.likes + likes
    except Exception:
        session.rollback()
        raise
    else:
        session.commit()
        session.close()
        return 1

# 根据userId查询跟帖评论
def selectFromXGetNSubReplyByUserId(userId, x, n):
    try:
        session = DBSession()
        offset = x
        num = x + n
        subreply = session.query(SubReply).filter(SubReply.userId == userId).order_by(SubReply.subreplyTime.desc()).slice(offset, num).all()
        if subreply is None:
            result = None
        else:
            result = subreply
    except Exception:
        raise
    else:
        session.close()
        return result

# 获取跟帖评论总数
def selectSumSubReply():
    result = 0
    try:
        session = DBSession()
        result = session.query(SubReply).count()
    except Exception:
        raise
    else:
        session.close()
        return result

# 获取用户的跟帖评论总数
def selectSumSubReplyByUserId(userId):
    result = 0
    try:
        session = DBSession()
        result = session.query(SubReply).filter(SubReply.userId == userId).count()
    except Exception:
        raise
    else:
        session.close()
        return result

# 获取某个跟帖的评论总数
def selectSumSubReplyByReplyId(replyId):
    result = 0
    try:
        session = DBSession()
        result = session.query(SubReply).filter(SubReply.replyId == replyId).count()
    except Exception:
        raise
    else:
        session.close()
        return result

# 根据跟帖评论ID查询跟帖评论
def selectSubReplyBySubReplyId(subreplyId):
    try:
        session = DBSession()
        subreply = session.query(SubReply).filter(SubReply.subreplyId == subreplyId).first()
        if subreply is None:
            result = None
        else:
            result = subreply
    except Exception:
        raise
    else:
        session.close()
    return result

# 删除跟帖的评论
def deleteSubReply(subreplyId):
    effect_raw = 0
    try:
        session = DBSession()
        subreply = session.query(SubReply).filter(SubReply.subreplyId == subreplyId).first()
        if subreply is None:
            effect_raw = 0
            return effect_raw
        else:
            session.query(SubReply).filter_by(subreplyId=subreplyId).delete()
            effect_raw = 1
    except:
        session.rollback()
        effect_raw = 0
    else:
        session.commit()
        session.close()
    return effect_raw