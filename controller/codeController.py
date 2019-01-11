from dao.sessionDao import redisCon
from email.mime.text import MIMEText
import hashlib
import random
import smtplib

from qcloudsms_py import SmsSingleSender
from qcloudsms_py.httpclient import HTTPError

# 密码加密
def encryption(password):
    hashPassword = hashlib.md5()
    hashPassword.update(password.encode(encoding='utf-8'))
    return hashPassword.hexdigest()

'''
# 发验证码（邮箱）
def sendEmail(tel):
    mail_host = "smtp.163.com"  # SMTP服务器
    mail_user = "zhuxiyulu@163.com"  # 用户名
    mail_pass = "zhuxi1430854887"  # 授权密码，非登录密码
    sender ="zhuxiyulu@163.com" # 发件人邮箱(最好写全, 不然会失败)
    receivers = tel  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    code = str(''.join(str(random.choice(range(10))) for _ in range(6)))
    exTime = int(5*60)
    try:
        redisCon.set(str(tel), str(code), ex=exTime)
        effect_row = 1
    except Exception:
        effect_row = 0
        raise
    content = '您的码为:'+code+"。有效时间5分钟，谢谢!\n<糖宝>"
    title = '有关糖'  # 邮件主题
    message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
    message['From'] = sender
    message['To'] = receivers
    message['Subject'] = title

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        effect_row = 1
    except smtplib.SMTPException as e:
        effect_row = 0

    return effect_row

'''


# 发验证码（短信）
def sendEmail(tel):
    appid = 1400101169;
    appkey = "905cac844a65ec9193513fd71e9d3283";
    phone_number = tel
    template_id = 137321
    ssender = SmsSingleSender(appid, appkey)

    code = str(''.join(str(random.choice(range(10))) for _ in range(6)))
    exTime = int(24*60*60)

    params = [code, "5"]

    try:
        result = ssender.send_with_param(86, phone_number, template_id, params)
        redisCon.set(str(tel), str(code), ex=exTime)
    except HTTPError as e:
        print(e)
    except Exception as e:
        print(e)
    return result



# 获取验证码
def getVerifyCode(tel):
    sendResult = sendEmail(tel)
    if sendResult['result'] == 0:
        data = {'code': 0}
    else:
        data = {'code': 1, 'msg': sendResult['errmsg']}
    return data