import smtplib
import random
import string
from email.mime.text import MIMEText

psw = []
r = []
rand = ''
final = ''
for i in range (0, 5, 1):
    
    string.ascii_letters 
    rletr = random.choice(string.ascii_letters)
    rnum = random.randint(0, 9)
    r.append(rletr)
    r.append(rnum)
    rand = random.choice(r)
    psw.append(rand)
    r.clear()
for i in psw:
    final+=str(i) #final is psw


subject = "Python psw"
body = "Tanii shine nuuts ug" + final
sender = "sw23d005@mandakh.edu.mn"
recipients = ["badmaarag.contact@gmail.com"]
password = "badmaarag12"


def send_email(subject, body, sender, recipients, password):
    for i in range(0, 2, 1):
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = ', '.join(recipients)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(sender, password)
            smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")


send_email(subject, body, sender, recipients, password)