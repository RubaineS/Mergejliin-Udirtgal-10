import smtplib
from email.mime.text import MIMEText

subject = "Python automatic email"
body = "This is just a test. For research purposes..."
sender = "sw23d005@mandakh.edu.mn"
recipients = ["badmaarag.contact@gmail.com"]
password = "badmaarag12"


def send_email(subject, body, sender, recipients, password):
    for i in range(0, 20, 1):
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = ', '.join(recipients)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(sender, password)
            smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")


send_email(subject, body, sender, recipients, password)
