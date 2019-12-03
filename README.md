# 中科大软件学院信息化平台消息订阅脚本

## 上手指南

本程序为基于python3爬虫的一个小的实用脚本，主要用来订阅中科大软件学院信息化平台发布的通知。方便在外地实习或者在校学业繁忙的小伙伴获取学校发布的最新通知。
以下将介绍脚本运行的环境，以及使用方法。

本人已经把脚本部署到个人服务器上，如果需要提供服务可以给我发送邮件：lysse@mail.ustc.edu.cn,主题为【订阅科软信息化平台】

## 运行环境

- python3

- requirements:

  ```python
    requests
    bs4
  ```

## 使用方法

- 下载代码

> $ git clone https://github.com/MoriatyBug/USTC_SSE_Message_Subscribe.git

- 修改conf.py
- 运行

> $ python notice_subscribe.py

![1575214034622.png](https://i.loli.net/2019/12/01/BJMQlTo9E1yuPkn.png)

![1575214116396.png](https://i.loli.net/2019/12/01/sKhX1na4peRY2Lu.png)

- shell脚本

> vim run.sh


```shell
#! /bin/bash
python3 notice_subscribe.py
```

> chmod +x run.sh

- 部署定时任务：
> $ crontab -e
> * * * * * root **/*.sh
> 时间      用户   脚本 (注意shell脚本需要有执行权限)
> /etc/init.d/crond restart
https://www.cnblogs.com/zishengY/p/6805316.html


## 发送邮件

- 问题1：容易发送失败
```shell
smtplib.SMTPDataError: (554, b'DT:SPM 163 smtp12,EMCowAA3o6zadeZdJwY6CA--.54140S2 1575384539,please see http://mail.163.com/help/help_spam_16.htm?ip=&hostid=smtp12&time=1575384539')
```
是因为163服务器把要发送的邮件当作垃圾邮件处理了，这个问题很恶心。因为你很难知道具体是哪里出错了。

- 问题2：群发单显
在群发邮件时为了保护隐私，我想收到邮件的用户只能在收件人一栏看到自己的邮箱。



## 后记

- 信息化平台的登录部分最让人头疼，首先是隐藏的表单信息，需要通过抓包工具来分析出来。
- 然后登录成功了，还不能实现自动跳转，需要自己指定url来跳转，一开始还以为爬虫出现了问题，仔细对比了response的头才发现登录成功了，然后尝试跳转到指定的url，结果成功了。
- 最新消息是根据当前时间来判断，因为我打算把脚本部署在服务器上，设置每天23:30运行一次，这样就可以得到当天最新的消息了。
- 然后调用邮件服务商提供的邮件服务，就可以愉快地发邮件了。