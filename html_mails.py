import smtplib
import ssl
from email.message import EmailMessage

sender_email="sender.mail@gmail.com"
receiver_email="reciever.mail@gmail.com"
app_password="your_app_password"
subject="hello this side ashis learning email automation with python "

html_content = """
<html>
  <body>
    <h2 style="color: blue;">Hello, dear friend!</h2>
    <p>This is a <b>HTML email</b> sent by <i>Ashis</i>.</p>
    <p>Click below to open google and learn python: </p>
    <a href='https://www.google.com'>Visit Google</a>
  </body>
</html>
"""  

email=EmailMessage()
email['from']=sender_email
email['to']=receiver_email
email['subject']=subject
email.set_content(html_content,subtype='html')

context=ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
    smtp.login(sender_email,app_password)
    smtp.send_message(email)

print("work done ")