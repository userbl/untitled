#!/usr/bin/python3

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host="smtp.sina.com"  #设置服务器
mail_user="bailongmail@sina.com"    #用户名
mail_pass="makelove"   #口令


sender = mail_user#'bailongmail@sina.com'
receivers = ['bailong@huihaiedu.net']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header(sender, 'utf-8')
message['To'] =  Header('bailong@huihaiedu.net', 'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')


try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, '25')    # 25 为 SMTP 端口号
    smtpObj.login(sender,mail_pass)
    smtpObj.sendmail(sender, 'bailong@huihaiedu.net', message.as_string())
    print ("邮件发送成功")
except smtplib.SMTPException as e :
    print(str(e))
    print ("Error: 无法发送邮件")