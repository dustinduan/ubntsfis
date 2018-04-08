import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
def mail(mailtext):
	sender='dustinduan2010@163.com'
	my_pass="accode1234"
	receiver='dustinduan2010@163.com'
    ret=True
    try:
        msg=MIMEText(mailtext,'plain','utf-8')
        msg['From']=formataddr(['dustin',sender])
        msg['To']=formataddr(['dustin',receiver])
        msg['Subject']="python邮件发送测试"
        server=smtplib.SMTP_SSL("smtp.163.com",465)
        server.login(sender,my_pass)
        server.sendmail(sender,[receiver],msg.as_string())
        server.quit()
    except Exception:
        ret=False
    return (ret)
ret=mail()
if ret:
    print("OK")
else:
    print("Fail")
c=input("stop")