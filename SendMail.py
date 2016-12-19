import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

with open("list.txt", 'r', encoding="utf8")as f:
    l = f.readlines()

maillist = [x[:-1].split("\t") for x in l]

def get_att(msg, url):
    att = MIMEText(open(url, 'rb').read(), 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    filename = url.split("/")[-1]
    att.add_header('content-disposition','attachment',filename=filename)
    msg.attach(att)



for mag in maillist:
    sender = 'Senders@mailaddress'
    mailto = mag[-1]

    #邮件信息
    msg = MIMEMultipart()
    msg['Subject'] = mag[0]
    msg['To'] = mailto
    msg['From'] = sender

    # 邮件内容
    Contents = MIMEText("htmlcode",
        'html')
    msg.attach(Contents)


# 带上附件

    if mag[3] == "1":
        no = 0
        for filename in os.listdir("期刊服务/"):
            if mag[0] == filename[:len(mag[0])]:
                get_att(msg, "期刊服务/" + filename)
                no += 1
        if no == 0:
            print(">>>>>>>>>>>>>>>>>>>>%s 没有找到文件！" % mag[0])
            continue
        if no > 1:
            print(">>>>>>>>>>>>>>>>>>>>%s 有多个对应文件！" % mag[0])
            continue
        print("=====")

    if mag[4] == "1":
        get_att(msg, "Attachment file 1")
        no += 1
    if mag[5] == "1":
        get_att(msg, "Attachment file 2")
        no += 1
    if mag[6] == "1":
        get_att(msg, "Attachment file 3")
        no += 1
    if mag[7] == "1":
        get_att(msg, "Attachment file 4")
        no += 1
    if mag[8] == "1":
        get_att(msg, "Attachment file 5")
        no += 1

    if no == 0:
        print("*******************%s 未发送，目的邮箱：%s" % (mag[0], mailto))
        continue


    #连接发送服务器
    smtp = smtplib.SMTP('server address')
    smtp.login("username", "passwords")

    #发送
    smtp.sendmail(sender,mailto,msg.as_string())
    smtp.quit()

    print("%s 发送完毕，目的邮箱：%s" % (mag[0], mailto))

