from domain.database import DBSession
from domain.comment import Comment
import datetime


# 添加评论
def insertComment(content, userId, articleId):
    effect_raw = 0
    try:
        session = DBSession()
        commentTime = datetime.datetime.now()
        adComment = Comment(content=content, userId=userId, articleId=articleId, commentTime=commentTime)
        session.add(adComment)
    except Exception:
        session.rollback()
        raise
    else:
        session.commit()
        session.close()
        effect_raw = 1
    return effect_raw

# 删除评论
def deleteComment(commentId):
    effect_raw = 0
    try:
        session = DBSession()
        comment = session.query(Comment).filter(Comment.commentId == commentId).first()
        if comment is None:
            effect_raw = 0
            return effect_raw
        else:
            session.query(Comment).filter_by(commentId=commentId).delete()
    except:
        session.rollback()
        effect_raw = 0
    else:
        effect_raw = 1
        session.commit()
        session.close()
    return effect_raw

# 根据文章查找评论
def selectCommentByArticle(articleId):
    result = []
    try:
        session = DBSession()
        comment = session.query(Comment).filter(Comment.articleId == articleId).all()
        if comment is None:
            result = None
        else:
            for i in range(len(comment)):
                result[i] = {'commentId': comment.commentId, 'content': comment.content, 'userId': comment.userId}
    except:
        session.rollback()
    else:
        session.close()
    return result

# 根据用户查找评论
def selectCommentByUser(userId, x, n):
    try:
        session = DBSession()
        offset = x
        num = x + n
        comment = session.query(Comment).filter(Comment.userId == userId).slice(offset, num).all()
        if comment is None:
            result = None
        else:
            result = comment
    except Exception:
        raise
    else:
        session.close()
    return result

# 从x位置获取文章articleId后面n篇评论
def selectFromXGetNCommentByArticleId(articleId, x, n):
    try:
        session = DBSession()
        offset = x
        num = x + n
        comment = session.query(Comment).filter(Comment.articleId == articleId).order_by(Comment.commentTime).slice(offset, num).all()
        if comment is None:
            result = None
        else:
            result = comment
    except Exception:
        raise
    else:
        session.close()
        return result

# 添加评论的点赞数
def updateLikes(commentId, isLike):
    try:
        session = DBSession()
        comment = session.query(Comment).filter(Comment.commentId == commentId).first()
        if comment is None:
            return 0
        else:
            comment.likes = comment.likes + isLike
    except Exception:
        session.rollback()
        raise
    else:
        session.commit()
        session.close()
        return 1

# 获取用户发表的评论总数
def selectSumCommentByUserId(userId):
    result = 0
    try:
        session = DBSession()
        result = session.query(Comment).filter(Comment.userId == userId).count()
    except Exception:
        raise
    else:
        session.close()
        return result

# 查看总共有多少个评论
def selectSumComment():
    result = 0
    try:
        session = DBSession()
        result = session.query(Comment).count()
    except Exception:
        raise
    else:
        session.close()
        return result

def selectSumCommentByArticleId(articleId):
    result = 0
    try:
        session = DBSession()
        result = session.query(Comment).filter(Comment.articleId == articleId).count()
    except Exception:
        raise
    else:
        session.close()
        return result