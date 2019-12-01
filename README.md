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



## 后记

- 信息化平台的登录部分最让人头疼，首先是隐藏的表单信息，需要通过抓包工具来分析出来。
- 然后登录成功了，还不能实现自动跳转，需要自己指定url来跳转，一开始还以为爬虫出现了问题，仔细对比了response的头才发现登录成功了，然后尝试跳转到指定的url，结果成功了。
- 最新消息是根据当前时间来判断，因为我打算把脚本部署在服务器上，设置每天23:30运行一次，这样就可以得到当天最新的消息了。
- 然后调用邮件服务商提供的邮件服务，就可以愉快地发邮件了。
