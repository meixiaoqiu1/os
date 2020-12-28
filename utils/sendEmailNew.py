import os
import smtplib
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class SendEmail(object):
    def __init__(self,username,passwd,recv,title,content,
                 ssl=False,email_host='smtp.126.com',port=25,ssl_port=465):
        self.username=username
        self.passwd=passwd
        self.recv=recv# 收件人，多个要传list ['a@qq.com','b@qq.com]
        self.title=title
        self.content=content
        self.email_host=email_host
        self.port=port
        self.ssl=ssl# 是否安全链接
        self.ssl_port=ssl_port# 安全链接端口

    def new_report(self, testreport):
        lists = os.listdir(testreport)
        # os.path.getmtime  获取文件的最终修改时间
        lists.sort(key=lambda fn: os.path.getmtime(testreport + '\\' + fn))
        file_new = os.path.join(testreport, lists[-1])
        return file_new
    def send_email(self,file):
        self.file=file
        # 创建一个带附件的实例
        msg=MIMEMultipart()
        #发送内容的对象
        if self.file:
            file_name=os.path.split(self.file)[-1]#取文件名
            try:
                f=open(self.file,'rb').read()
                #构造附件
                att=MIMEText(f,"base64","utf-8")
                att["Content-Type"]='application/octet-stream'
                new_file_name='=?utf-8?b?'+base64.b64encode(file_name.encode()).decode()+'?='
                #这里是处理文件名为中文名的，必须这么写
                att['Content-Disposition']='attachment;filename="%s"'%(new_file_name)
                msg.attach(att)

            except Exception as e:
                raise Exception('附件打不开！')

        msg.attach(MIMEText(self.content))#邮件正文内容
        msg['Subject']=self.title #邮件主题
        msg['From']=self.username
        msg['To']=','.join(self.recv)#接收者账号列表
        if self.ssl:
            self.smtp=smtplib.SMTP_SSL(self.email_host,port=self.ssl_port)
        else:
            self.smtp=smtplib.SMTP(self.email_host,port=self.port)
        #发送邮件服务器的对象
        self.smtp.login(self.username,self.passwd)
        try:
            self.smtp.sendmail(self.username,self.recv,msg.as_string())
            print('发送成功！')
            self.smtp.quit()
        except Exception as e:
            print('出错了。。',e)
            self.smtp.quit()
