# 本程序用于邮件订阅中科大软件学院信息化平台最新发布的消息
# 方便在外实习或者学业繁忙的同学能实时关注学校官网发送的通知
# 如需订阅请发送邮件到lysse@mail.ustc.edu.cn,主题为【订阅科软信息化平台】
from conf import *
import requests
from bs4 import BeautifulSoup
import datetime
import smtplib
from email.mime.text import MIMEText

USTC_SSE_URL = "http://mis.sse.ustc.edu.cn/default.aspx"
HEADER = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
}
valid_url = "http://mis.sse.ustc.edu.cn/ValidateCode.aspx?ValidateCodeType=1&0.0214071427571621"
SESSION = requests.Session()
BASE_URL = "http://mis.sse.ustc.edu.cn/"


def get_sum(valid_sums):
    """
    计算验证码结果
    """
    res = 0
    for i in valid_sums:
        res += int(i)
    return res

def get_update_notice():
    """
    获取最新的通知
    """
    resp = SESSION.get(valid_url, headers=HEADER)
    valid_nums = resp.cookies.get_dict()['CheckCode']
    sum_res = get_sum(valid_nums)
    user_id = USER_ID
    user_pwd = USER_PWD
    # 登录所需form信息
    data = {
        '__EVENTTARGET' : 'winLogin$sfLogin$ContentPanel1$btnLogin',
        '__EVENTARGUMENT' : '',
        '__VIEWSTATE' : '/wEPDwUKLTMzNjg2NDcwNGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgwFCHdpbkxvZ2luBRB3aW5Mb2dpbiRzZkxvZ2luBRZ3aW5Mb2dpbiRzZkxvZ2luJGN0bDAwBR93aW5Mb2dpbiRzZkxvZ2luJHR4dFVzZXJMb2dpbklEBRx3aW5Mb2dpbiRzZkxvZ2luJHR4dFBhc3N3b3JkBRx3aW5Mb2dpbiRzZkxvZ2luJHR4dFZhbGlkYXRlBR53aW5Mb2dpbiRzZkxvZ2luJENvbnRlbnRQYW5lbDMFLHdpbkxvZ2luJHNmTG9naW4kQ29udGVudFBhbmVsMyRjYnhTYXZlTXlJbmZvBS53aW5Mb2dpbiRzZkxvZ2luJENvbnRlbnRQYW5lbDMkYnRuUmVmVmFsaWRDb2RlBR53aW5Mb2dpbiRzZkxvZ2luJENvbnRlbnRQYW5lbDEFJ3dpbkxvZ2luJHNmTG9naW4kQ29udGVudFBhbmVsMSRidG5Mb2dpbgUIV25kTW9kYWwAzaTak4Gu+DOPx1c51GwX60AZ8Mdx0PxBzyDcSqbllw==',
        'X_CHANGED' : 'true',
        'winLogin$sfLogin$txtUserLoginID' : user_id,
        'winLogin$sfLogin$txtPassword' : user_pwd,
        'winLogin$sfLogin$txtValidate' : sum_res,
        'winLogin_Hidden' : 'false',
        'WndModal_Hidden' : 'true',
        'X_TARGET' : 'winLogin_sfLogin_ContentPanel1_btnLogin',
        'winLogin_sfLogin_ctl00_Collapsed' : 'false',
        'winLogin_sfLogin_ContentPanel3_Collapsed' : 'false',
        'winLogin_sfLogin_ContentPanel1_Collapsed' : 'false',
        'winLogin_sfLogin_Collapsed' : 'false',
        'winLogin_Collapsed' : 'false',
        'WndModal_Collapsed' : 'false',
        'X_STATE' : 'eyJ3aW5Mb2dpbl9zZkxvZ2luX2N0bDAwX2xiTXNnIjp7IlRleHQiOiLluJDlj7flr4bnoIHkuI3og73kuLrnqboifX0=',
        'X_AJAX' : 'true',
    }
    SESSION.post(USTC_SSE_URL, data=data, headers=HEADER)
    stuChoosedUrl = 'http://mis.sse.ustc.edu.cn/homepage/StuHome.aspx'
    response2 = SESSION.get(stuChoosedUrl, headers=HEADER)
    soup = BeautifulSoup(response2.content.decode(), 'html.parser')
    notice_node = soup.find('div',id="global_LeftPanel_UpRightPanel_ContentPanel2_ContentPanel3_content")
    
    notice_nodes = notice_node.find_all("tr")
    notice_list = []
    for node in notice_nodes:
        notice_dict = dict()
        print(node.find_all("td")[0].text)
        notice_dict["title"] = node.find_all("td")[0].text
        notice_dict["link"] = node.find_all("td")[0].a["href"]
        notice_dict["time"] = node.find_all("td")[2].text
        notice_dict["author"] = node.find_all("td")[1].text
        notice_list.append(notice_dict)
    print(notice_list)
    send_notice(notice_list)


def send_notice(notice_list):
    print("*************正在发送邮件************")
    year  = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day   = datetime.datetime.now().day
    cur_date = "" + str(year) + "-" + str(month) + "-" + str(day)
    for notice in notice_list:
        if notice["time"] == cur_date:
            notice["content"] = get_notice_content(notice["link"])
            send_email(notice)


def get_notice_content(_notice_url):
    """
    获取通知内容
    """
    notice_url = BASE_URL + _notice_url
    resp = SESSION.get(notice_url, headers=HEADER)
    return resp.content.decode()


def send_email(_notice):
    """
    发送邮件通知
    """
    host = HOST
    port = 25
    sender = SENDER
    pwd = SMTP_PWD
    body = _notice["content"]
    msg = MIMEText(body, 'html')
    msg['subject'] = "【" + _notice["title"] + "】" + "-" + _notice["author"]
    msg["from"] = sender
    msg["to"] = ';'.join(RECEIVER)
    s = smtplib.SMTP(host, port)
    s.login(sender, pwd)
    s.sendmail(sender, RECEIVER, msg.as_string())
    print("*****************邮件发送成功*******************")
    

def main():
    get_update_notice()
    

if __name__ == "__main__":
    main()