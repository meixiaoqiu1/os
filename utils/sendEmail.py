# -*- coding:utf-8-*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os

class SendEmail():
    # ==========定义发送邮件============

    def send_mail(self,file_new):
        f = open(file_new, 'r',encoding='utf-8')
        mail_body = f.read()
        f.close()

        FROM = "shemeiqiong@126.com"
        PWD='TSVSWNMMIHUDHUYY'
        # TO = "cai_j@720wan.com,chang_f@720wan.com, duan_w@720wan.com, li_h@720wan.com"
        TO = 'xiaomeiqiu111@126.com'

        msg = MIMEText(mail_body, 'html', 'utf-8')
        msg['Subject'] = Header("接口自动化测试报告", 'utf-8')
        msg['From'] = FROM
        msg['To'] = TO

        smtp = smtplib.SMTP()
        smtp.connect('smtp.126.com')
        smtp.login(FROM, PWD)
        smtp.sendmail(FROM, TO, msg.as_string())
        smtp.quit()
        print('email has send out!')

    # ====查找测试报告目录，找到最新生成的测试报告文件============

    def new_report(self,testreport):
        lists = os.listdir(testreport)
        # os.path.getmtime  获取文件的最终修改时间
        lists.sort(key=lambda fn: os.path.getmtime(testreport + '\\' + fn))
        file_new = os.path.join(testreport, lists[-1])
        return file_new