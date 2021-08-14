from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import json


class SMTPConfig():
    def __init__(self, path, conf_type=""):
        f = open(path, 'r')
        smtp_str = f.read()
        self.select = conf_type
        self.info = json.loads(smtp_str)
        print("Step 2: Init The Configure Info")

    def GetMailHostServer(self):
        print()

    def GetMailTitle(self):
        print()

    def GetMailReceiver(self):
        print()

    def GetMailSender(self):
        print()

    def GetMailSenderPwd(self):
        print()

    def GetMailContent(self):
        print()


class SMTPManger():

    def __init__(self, conf_path="", conf_type=""):
        print("Init The Confure Info")
        self.__config = SMTPConfig(conf_path, conf_type)

    def CreateSMTPInfo(self, type=""):
        msg = MIMEMultipart()
        # 1. 建立邮箱的标题
        msg["Subject"] = Header(self.__config.GetMailTitle(), 'utf-8')
        # 2. 建立邮箱的发件人
        msg["From"] = self.__config.GetMailReceiver()
        # 3. 建立邮箱的收件人
        msg['To'] = self.__config.GetMailReceiver()
        # 4. 建立邮箱的正文
        msg.attach(MIMEText(self.__config.GetMailContent(), 'plain', 'utf-8'))
        # 5. 建立邮件的附件

        return msg

    def Login(self):
        smtp = SMTP_SSL(self.__config.GetMailHostServer())
        sender = self.__config.GetMailSender()
        pwd = self.__config.GetMailSenderPwd()
        smtp.login(sender, pwd)
        return smtp

    def SendSMTP(self):

        smtp = self.Login()

        msg = self.CreateSMTPInfo()

        sender = self.__config.GetMailSender()
        receivers = self.__config.GetMailReceiver()
        receiver = receivers.split(';')

        # 6. 发送邮件
        smtp.sendmail(sender, receiver, msg.as_string())
        # 7. 退出
        smtp.quit()


if __name__ == '__main__':

    print("Step 1: Init The SMTP Manager")

    manager = SMTPManger()
    manager.SendSMTP()

    print("Finish")
