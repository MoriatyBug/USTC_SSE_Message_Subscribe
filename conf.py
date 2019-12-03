# -*- coding: utf-8 -*-

# 设置订阅人的邮箱
RECEIVER = ['**@**']

# 信息化平台的用户名和密码
USER_ID  = "SA****"
USER_PWD = "***"

# 是否在实习，用于提醒写实习月报，后期建立receiver的字典保存，目前没有必要
IS_INTERNSHIP = True

# SMTP服务器信息设置（发件邮箱）
# 我用的是163邮箱
# 可以参考：https://blog.csdn.net/qlzy_5418/article/details/86661883
HOST   = "smtp.163.com" # SMTP服务器host
SENDER = "***@163.com" # SENDER为自己的邮箱名
SMTP_PWD = "***" # 密码为smtp服务器的授权码，需要到邮箱上设置。 跟登陆密码不一样！*3