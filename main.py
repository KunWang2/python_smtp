from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import json
import sys


class SMTPConfig():
    def __init__(self, path, conf_type=""):
        f = open(path, 'r', encoding='utf-8')
        smtp_str = f.read()
        self.select = conf_type
        self.info = json.loads(smtp_str)
        self.dict_info = self.info.get(conf_type)
        if self.dict_info is None:
            print("Please Check the Conf Type ")
        print("Step 2: Init The Configure Info")

    def GetMailHostServer(self):
        return self.dict_info["hostserver"]
        print()

    def GetMailTitle(self):
        return self.dict_info["title"]
        print()

    def GetMailReceiver(self):
        return self.dict_info["receiver"]
        print()

    def GetMailSender(self):
        return self.dict_info["sender"]
        print()

    def GetMailSenderPwd(self):
        return self.dict_info["password"]
        print()

    def GetMailContent(self):
        return self.dict_info["content"]
        print()

    def GetMailPort(self):
        return self.dict_info["hostport"]


class SMTPManger():

    def __init__(self, conf_path="", conf_type=""):
        print("Init The Confure Info")
        self.__config = SMTPConfig(conf_path, conf_type)

    def CreateSMTPInfo(self):
        msg = MIMEMultipart()
        # 1. 建立邮箱的标题
        msg["Subject"] = Header(self.__config.GetMailTitle(), 'utf-8')
        # 2. 建立邮箱的发件人
        msg["From"] = self.__config.GetMailSender()
        # 3. 建立邮箱的收件人
        msg['To'] = self.__config.GetMailReceiver()
        # 4. 建立邮箱的正文
        msg.attach(MIMEText(self.__config.GetMailContent(), 'plain', 'utf-8'))
        # 5. 建立邮件的附件

        return msg

    def Login(self):
        smtp = SMTP_SSL(self.__config.GetMailHostServer(), self.__config.GetMailPort())
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

    path = "./conf/mail.json"
    # 修改成入参指定
    select_type = "marsol"
    if len(sys.argv) > 1 :
        select_type = sys.argv[1]

    manager = SMTPManger(path, select_type)
    manager.SendSMTP()

    print("Finish")
 