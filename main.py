import os
import smtplib
from email.message import EmailMessage

SENDER = "placeholder@gmail.com" #TODO: Gmail 
PASSWORD = os.environ.get("GMAIL_APP_PASSWORD")  #TODO: Gmail Authentication

msg = EmailMessage()
msg["Subject"] = ... #TODO: a test subject
msg["From"] = SENDER
msg["To"] = ... #TODO: send it to myself for now
msg.set_content(...) #TODO: the message body

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(SENDER, PASSWORD)
    server.send_message(msg)

print("Sent!")